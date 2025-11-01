def gcd(a, b):
    while b != 0:
        a, b = b, a % b # a % b < b, więc zawsze pierwsza liczba jest wieksza
    return a

def change_base(n, k):
    mult = 1
    nr = 0
    while True:
        nr += 1
        if mult * k > n:
            break # jeśli po kolejnym mnożeniu dostalibyśmy coś większego to wychodzimy, żeby potem po pętli nie musieć dzielić
        mult *= k
 
    converted = [0 for _ in range(nr)]

    for i in range(nr):
        x = n//mult # ile razy dana potęga się mieści w liczbie, zaczyna od najwiekszych
        converted[i] = x # zapisujemy w naszym systemie
        n -= mult * x # odejmujemy od liczby tyle ile razy ta potęga się mieści
        mult //= k # idziemy z potęgą o 1 stopień nizej
    
    return converted


def get_best_partition(num:list[int], k:int):
    best_res, best_p = 0, -1 # najlepszy wynik i indeks podziału

    left = [0 for _ in range(len(num))] # będziemy liczyć z 2 stron osobno, więc jedna musi być zapamiętana
    best_right = -1 # left mamy w tablicy a dla right potrzebujemy tylko 1 najlepsza wartosc
    for p in range(len(num) - 1): # liczba left policzona od lewego końca do elementu p, idziemy od 0 do przedostatniego
        left[p] = left[p-1] * k + num[p] 
        # przesuniecie liczby w prawo w systemie o podstawie k i dodanie kolejnej liczby na koniec
        # czyli np chcemy z 23 w podstawie 5 zrobić 234, wtedy potęgi przy 2 i 3 podnoszą się o 1
        # i jeszcze musimy dodać 4 (bo samo podniesienie potęg to tak jakby dodanie 0 na końcu)

    temp_right_res = 0
    mult = 1
    for p in range(len(num) - 1, 0, -1): # idziemy od końca do 1
        temp_right_res += mult * num[p] # aktualnie policzona liczba idąc od prawej strony
        temp_res = left[p-1] * temp_right_res # korzystamy z wcześniej policzonego wyniku left dla pozostałej części liczby (stąd left[p-1]) i
                                            # obliczamy iloczyn 'left_res * right_res'

        if gcd(temp_right_res, left[p-1]) == 1 and temp_res > best_res: # warunek z zadania
            best_res = temp_res # uaktualniamy najwiekszy wynik
            best_p = p # zapisujemy punkt podzialu
            best_right = temp_right_res # zapisujemy wynik od prawej strony zeby moc pozniej go zwrocic, jak znajdziemy cos lepszego iloczynowo
                                        # pozniej to on sie tez zmieni
        mult *= k
    return best_res, best_p, left[best_p - 1], best_right # znając najlepszy punkt p mozna latwo znalezc ile dla niego wynosi left


def solve(N):
    act_max_res = 0
    act_best_base = -1
    for b in range(2, 17):
        conv:list[int] = change_base(N, b)
        res, p, left_dec, right_dec = get_best_partition(conv, b)
        if res > act_max_res:
            act_max_res = res
            act_best_base = b

            print("podstawa: ", b)
            print(conv[:p], conv[p:]) # mamy punkt podziału to wypisujemy tablice left i right (dalej w systemie o podstawie b)
            print(f"{left_dec} * {right_dec} = {act_max_res}")
            print()

    print(f"Otrzymana najlepsza podstawa: {act_best_base}")
    print(f"Otrzymany dla niej wynik: {act_max_res}")


for n1 in [141, 202, 10092392]:
    print("-" * 100)
    print(f"LICZBA: {n1}\n")
    solve(n1)
    print("\n")