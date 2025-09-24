__all__ = ['novy_seznam2']

from . import slovnik2  # import z vedlejsiho modulu v tomto balicku
from ..soubory2 import zapis2  # import z vedlejsiho subbalicku
from ..obecne2  import napis_pisemku2   # import z nadazeneho balicku

# modul pro praci se seznamy
def novy_seznam2():
    print('funkce na novy seznam')

def otoc_seznam2():
    print('funkce na otoceni seznamu')

def pouzij_relativni_import():
    slovnik2.novy_slovnik2()
    zapis2.zapis_text2()
    napis_pisemku2()
    