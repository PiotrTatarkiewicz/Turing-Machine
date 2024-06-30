from SortAscendingController import SortAscendingController
from TuringMachine import TuringMachine

"""
Tworzona jest instancja klasy TuringMachine reprezentująca maszynę Turinga.
Pierwszym argumentem jest klasa implementująca Controller, dla której zostanie stworzona instancja i będzie ona użyta do wykonywania akcji.
Drugim argumentem jest taśma maszyny przedstawiona jako tablica jednowymiarowa.
Trzecim argumentem jest indeks, określający początkowe położenie głowicy.
Czwartym argumentem jest znak, który jest używany do określania pustych komórek.
"""
machine = TuringMachine(SortAscendingController, ['3', '4', '1', '2', '2', '4', '3', '2', '3', '1', '3', '2'], 0, '#')
machine.enable()
