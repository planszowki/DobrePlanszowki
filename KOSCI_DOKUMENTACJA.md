Gra, uruchamiana z pliku gra_kosci.py poprzez komendę python gra_kosci.py, jest symulatorem gry w kości umożliwiającym rozgrywkę zarówno w trybie single player, z komputerowymi przeciwnikami, jak i multiplayer.
Interfejs jest łatwy i intuicyjny, a dzięki uruchamianiu w terminalu wymagania sprzętowe są niemal znikome. Poza jednym ważnym elementem.
Komputer musi posiadać zainstalowane środowisko Python 3.7 oraz biblioteki pandas i matplotlib.
Dla zwiększenia dynamiki i tempa rozrywki w przypadku graczy sterowanych przez sztuczną inteligencję prezentowany jest jedynie efekt danej kolejki.
Użytkownicy posiadają możliwość ustawienia atrybutów graczy komputerowych, których decyzje niejednokrotnie mogą być zaskakujące, co tylko dodaje uroku rozgrywkom.

Kwestie dotyczące rozgrywki
Każda próba w grze w kości składa się z trzech rzutów pięcioma tradycyjnymi kośćmi.
Gracz może wymieniać kości między rzutami, może również zrezygnować z dalszych rzutów w ramach swojej próby.
Jeśli zdecyduje się na wpisanie wyniku po pierwszym rzucie, wartość zostanie podwojona. Jednak musi być ostrożny w podejmowaniu tego ryzyka - podwojeniu ulegają również ujemne wyniki.
W ramach jednej kolumny gracz podchodzi do siedemnastu prób.

W pierwszych sześciu wierszach znajdują się wartości z tak zwanej szkoły.
Jeśli gracz wyrzuci trzy kości z daną liczbą oczek, to otrzymuje punkt, który może wpisać do danej kolumny.
Jeśli więcej, to otrzymuje dodatkowe punkty. Jeśli mniej, to punkty są odejmowane.
Szczegółowy algorytm jest opisany w komentarzach do pliku kombinacje.py.
W przypadku uzyskania co najmniej 15 punktów w danej kolumnie, to gracz uzyskuje premię w wysokości 50 punktów.
Należy pamiętać o tym, że złe występy są również karane. Zakończenie szkoły z saldem minus 10 punktów kończy się odjęciem kolejnych 50.

Oprócz szkoły dostępne są również inne kombinacje do wpisania.
Są to para, dwie pary, trójka (trzy kości z daną liczbą oczek w jednym rzucie), mały strit (kombinacja 1-2-3-4-5), duży strit (kombinacja 2-3-4-5-6), parzyste (wszystkie kości w rzucie muszą mieć parzystą liczbę oczek), nieparzyste (wszystkie kości w rzucie muszą mieć nieparzystą liczbę oczek), ful (trzy kości o tych samych oczkach i dwie również równe sobie), kareta (cztery kości o tych samych oczkach), generał (wszystkie kości o tych samych oczkach) i szansa (suma wyrzuconych kości).

Jeśli graczowi nie uda się uzyskać wartości pozwalającej na wpisanie którejkolwiek z powyższych kombinacji, musi dokonać skreślenia z grona tych, które pozostały mu do rzucenia. Oznacza to, że nie będzie mógł jej rzucić w ramach danej kolumny, dodatkowo uzyskuje -10 punktów. Oczywiście nie ograniczamy się wyłącznie do negatywnych aspektów. Jeśli graczowi uda się rzucić wszystkie kombinacje w kolumnie bez skreśleń, uzyskuje dodatkowe 50 punktów.

Kwestie techniczne
Program składa się z czterech klas:

gra_kosci.py - głównego pliku koniecznego do uruchomienia gry
gracz.py - z parametrami na temat graczy, zawiera również klasę dziedziczącą GraczKomputerowy
rozgrywka.py - odpowiadająca za wyświetlanie i pobieranie informacji od gracza w trakcie danej próby
kombinacje.py - odpowiadająca za obsługę danych kombinacji
W kodzie starano się wykorzystać wszystkie rzeczy, które były omawiane na zajęciach.
Dlatego m.in. w ramach klasy Kombinacje w metodach stosowane są różne sposoby na sprawdzenie, czy rzucone kości pasują do danej kombinacji.

Uruchomienie gry: python gra_kosci.py

Wymagane środowisko: Python 3.7 z bibliotekami pandas i matplotlib.
