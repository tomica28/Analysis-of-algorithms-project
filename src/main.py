from solver_class import Solver
from generator_class import Generator
import argparse
import time
import sys
import simple_max



def mediana(k, list, list_T):
    if(k%2 == 0):
        med_T = (list_T[int(k/2)]+list_T[int(k/2 - 1)])/2
        med = (list[int(k/2)]+list[int(k/2 - 1)])/2
        return med_T/med
    else:
        return list_T[int((k-1)/2)]/list[int((k-1)/2)]


def main():
    parser = argparse.ArgumentParser(description='AAL gra na gieldzie')
    parser.add_argument('-m1', '--mode1_list', nargs='+', help='<Required> Set flag')
    parser.add_argument('-m2', '--mode2', action='store_true', help='turn on mode 2' )
    parser.add_argument('-m3', '--mode3', action='store_true', help='turn on mode 3')
    parser.add_argument('-n', '--number', action='store', type=int, help='Number of shares')
    parser.add_argument('-d', '--probability', action='store', type=float, help='Probability of increasing function')
    parser.add_argument('-k', '--num_problems', action='store', type=int, help='Number of problems')
    parser.add_argument('-step', '--step', action='store', type=int, help='Step size')
    parser.add_argument('-r', '--same_n', action='store', type=int, help='Number of problems with the same n')
    parser.add_argument('-g', '--generator', action='store', type=int, choices=range(3), help='Generator mode')
    parser.add_argument('-low', '--lower_price', action='store', type=int, help='Lower bound of share price')
    parser.add_argument('-up', '--upper_price', action='store', type=int, help='Upper bound of share price')
    parser.add_argument('-rand_para', '--rand_parametr', action='store', type=int, help='Parametr for the hardest test')

    args = parser.parse_args()
    solver = Solver
    gen = Generator
    g = args.generator
    n = args.number
    d = args.probability
    k = args.num_problems
    step = args.step
    r = args.same_n
    low = args.lower_price
    up = args.upper_price
    rand_para = args.rand_parametr
    if(low != None and up != None and low > up):
        sys.stderr.write("Up must be higher than low")
        sys.exit(-1)

    if not(args.mode1_list is None):
        list = [int(i) for i in args.mode1_list]
        print("Lista akcji: " + str(list))
        print("Wynik: " + str(solver.collecting_shares(solver, list)))
    if args.mode2:
        if(n == None):
            sys.stderr.write("N is required in this mode")
            sys.exit(-1)
        else:
            if(g == 0 and rand_para == None):
                sys.stderr.write("Rand_para is required in this mode")
                sys.exit(-1)
            elif((g == 1 or g == 2) and (low == None or up == None or d == None)):
                sys.stderr.write("Low, up, d are required in this mode")
                sys.exit(-1)
            elif(g == None):
                sys.stderr.write("G is required in this mode")
                sys.exit()
        list =[]
        if(g == 0):
            list = gen.hardest_test(gen, n, rand_para)
        elif(g == 1):
            list = gen.generate_decreasing(gen, n, low, up, d)
        else:
            list = gen.generate(gen, n, low, up, d)
        print("Lista akcji: " +str(list))
        print("Wynik: " + str(solver.collecting_shares(solver,list)))
    if args.mode3:
        if (n == None or k == None or step == None or r == None):
            sys.stderr.write("N is required in this mode")
            sys.exit(-1)
        else:
            if (g == 0 and rand_para == None):
                sys.stderr.write("Rand_para is required in this mode")
                sys.exit(-1)
            elif ((g == 1 or g == 2) and (low == None or up == None or d == None)):
                sys.stderr.write("Low, up, d are required in this mode")
                sys.exit(-1)
            elif(g == None):
                sys.stderr.write("G is required in this mode")
                sys.exit()
        times = []
        for i in range(k):
            list =[]
            for j in range(r):
                if (g == 0):
                    list.append(gen.hardest_test(gen, n+i*step, rand_para))
                elif (g == 1):
                    list.append(gen.generate_decreasing(gen, n+i*step, low, up, d))
                else:
                    list.append(gen.generate(gen, n+i*step, low, up, d))
            t = time.process_time_ns()
            for j in range(r):
                #result = solver.collecting_shares(solver,list[j])
                result = simple_max.simple_collecting(list[j])
            t_result = time.process_time_ns() - t
            times.append(t_result/r)
        T_list = []
        for i in range(k):
            temp = n+step*i
            T_list.append((temp*(temp+2))/2)
        print("N:       t(n)[ns]:       q(n):")
        med = mediana(k, times, T_list)
        for i in range(k):
            temp = (times[i]/T_list[i])*med
            print(str(n+step*i) + "\t" + str(times[i]) )

if __name__ == '__main__':
    main()