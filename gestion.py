from lycee import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import pymysql

class ApplicationIHM(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.score = 0
        self.fill_combobox_3()
        self.fill_combobox()
        self.fill_combobox_2()
        self.fill_combobox_4()
        self.fill_combobox_5()

    def fill_linedit_2(self):
        eleve = self.ui.comboBox_4.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        id_classe = f"select id_classe from eleves where nom = '{eleve}'"
        requete = f"select Classe from classes where id_classe in( {id_classe})"
        cur.execute(requete)
        classe = cur.fetchall()[0][0]
        con.close()
        self.ui.lineEdit_2.setText(classe)

    def fill_combobox_4(self):
        self.ui.comboBox_4.clear()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        requete = "select nom from eleves"
        cur.execute(requete)
        eleves = cur.fetchall()
        con.close()
        index = 1
        for eleve in eleves:
            self.ui.comboBox_4.insertItem(index, eleve[0])
            index += 1

    def fill_combobox_3(self):
        self.ui.comboBox_3.clear()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        requete = "select Classe from classes"
        cur.execute(requete)
        classes = cur.fetchall()
        con.close()
        self.ui.comboBox_3.clear()
        index = 1
        for classe in classes:
            self.ui.comboBox_3.insertItem(index, classe[0])
            index += 1

    def fill_combobox(self):
        self.ui.comboBox.clear()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        cur.execute('SELECT nom FROM disciplines')
        resultat = cur.fetchall()
        con.close()
        index = 1
        for nom in resultat:
            self.ui.comboBox.insertItem(index, nom[0])
            index += 1

    def fill_combobox_2(self):
        self.ui.comboBox_2.clear()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        cur.execute('SELECT nom FROM profs')
        resultat = cur.fetchall()
        con.close()
        index = 1
        for nom in resultat:
            self.ui.comboBox_2.insertItem(index, nom[0])
            index += 1

    def eleve(self):
        self.fill_linedit_2()
        self.fill_etudes()
        self.fill_notes()


    def prof(self):
        self.fill_disciplines()
        self.fill_classes()
        self.fill_cours()

    def classe(self):
        self.fill_eleves()
        self.fill_professeurs()
        self.fill_discipline()

    def notes_classes(self):
        self.fill_combobox_6()
        self.fill_combobox_7()
        self.fill_combobox_8()

    def fill_combobox_8(self):
        index_cours1 = self.ui.comboBox_7.currentText()
        id=''
        for c in index_cours1:
            if c == ' ':
                break
            else:
                id += c
        id_cours = int(id)
        classe = self.ui.comboBox_5.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        requete = f"select id_devoir, date from devoirs where id_cours = {id_cours}"
        cur.execute(requete)
        devoirs = cur.fetchall()
        self.ui.comboBox_8.clear()
        index = 1
        for devoir in devoirs:
            item = f"{devoir[0]}  {devoir[1]}"
            self.ui.comboBox_8.insertItem(index, item)

    def update_note(self):
        index_devoir_1 = self.ui.comboBox_8.currentText()
        print(index_devoir_1)
        id = ''
        for c in index_devoir_1:
            if c == ' ':
                break
            else:
                id += c
        print(id)
        if id != '':
            id_devoir = int(id)
        else:
            id_devoir = 0
        eleve1 = self.ui.comboBox_6.currentText()
        eleve = ''
        for c in eleve1:
            if c == ' ':
                break
            else:
                eleve += c

        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        cur.execute(f"select id_eleve from eleves where nom = '{eleve}'")
        resultat = cur.fetchall()
        print(resultat)
        id_eleve = resultat[0][0]
        requete = f"select note from notes where id_eleve = '{id_eleve}' and id_devoir = {id_devoir}"
        cur.execute(requete)
        note = cur.fetchall()
        if note:
            self.ui.lineEdit_3.setText(str(note[0][0]))

    def update_devoirs(self):
        self.fill_combobox()

    def fill_combobox_5(self):
        requete = "select Classe from classes"
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        cur.execute(requete)
        classes = cur.fetchall()
        self.ui.comboBox_5.clear()
        index = 1
        for classe in classes:
            self.ui.comboBox_5.insertItem(index, classe[0])
            index += 1
        con.close()

    def fill_notes(self):
        eleve = self.ui.comboBox_4.currentText()
        id_eleve = f"select id_eleve from eleves where nom = '{eleve}'"
        id_notes = f"select id_note from notes where id_eleve in ({id_eleve})"
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        requete = f"SELECT notes.note, disciplines.nom, profs.nom FROM notes, disciplines, profs, devoirs, cours where notes.id_note in ({id_notes}) and notes.id_devoir = devoirs.id_devoir and devoirs.id_cours = cours.id_cours and cours.id_prof = profs.id_prof and cours.id_discipline = disciplines.id_discipline"
        cur.execute(requete)
        notes = cur.fetchall()
        self.ui.listWidget_9.clear()
        for note in notes:
            item = str(note[0]) + "  " + note[1] + "  " + note[2]
            self.ui.listWidget_9.addItem(item)
        con.close()

    def fill_etudes(self):
        eleve = self.ui.comboBox_4.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        id_classe = f"select id_classe from eleves where nom = '{eleve}'"
        id_cours = f"select id_cours from cours where id_classe in ({id_classe})"
        requete = f"select disciplines.nom, profs.nom from disciplines, profs, cours where cours.id_cours in ({id_cours}) and disciplines.id_discipline = cours.id_discipline and cours.id_prof = profs.id_prof"
        cur.execute(requete)
        cours = cur.fetchall()
        self.ui.listWidget_8.clear()
        for cour in cours:
            item = cour[0] + "  " + cour[1]
            self.ui.listWidget_8.addItem(item)
        con.close()

    def fill_discipline(self):
        classe = self.ui.comboBox_3.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        id_classe = f"select id_classe from classes where Classe = '{classe}'"
        id_disciplines = f"select id_discipline from cours where id_classe in ({id_classe})"
        requete = f"select nom from disciplines where id_discipline in ({id_disciplines})"
        cur.execute(requete)
        disciplines = cur.fetchall()
        self.ui.listWidget_7.clear()
        for discipline in disciplines:
            self.ui.listWidget_7.addItem(discipline[0])
        con.close()


    def fill_professeurs(self):
        classe = self.ui.comboBox_3.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        id_classe = f"select id_classe from classes where Classe = '{classe}'"
        id_profs = f"select id_prof from cours where id_classe in ({id_classe})"
        requete = f"select nom, prenom from profs where id_prof in ({id_profs})"
        cur.execute(requete)
        profs = cur.fetchall()
        self.ui.listWidget_6.clear()
        for prof in profs:
            item = prof[0] + "  " + prof[1]
            self.ui.listWidget_6.addItem(item)
        con.close()


    def fill_eleves(self):
        classe = self.ui.comboBox_3.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        id_classe = f"select id_classe from classes where Classe = '{classe}'"
        requete = f"select nom, prenom from eleves where id_classe in ({id_classe})"
        cur.execute(requete)
        eleves = cur.fetchall()
        self.ui.listWidget_5.clear()
        for eleve in eleves:
            nom = eleve[0]
            prenom = eleve[1]
            item = nom + "  " + prenom
            self.ui.listWidget_5.addItem(item)
        con.close()

    def fill_combobox_6(self):
        classe = self.ui.comboBox_5.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        id_classe = f"select id_classe from classes where Classe = '{classe}'"
        requete = f"select nom, prenom from eleves where id_classe in ({id_classe})"
        cur.execute(requete)
        eleves = cur.fetchall()
        self.ui.comboBox_6.clear()
        index = 1
        for eleve in eleves:
            item = eleve[0]+"  "+ eleve[1]
            self.ui.comboBox_6.insertItem(index, item)
            index += 1
        con.close()

    def fill_combobox_7(self):
        classe = self.ui.comboBox_5.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        id_classe = f"select id_classe from classes where Classe = '{classe}'"
        requete = f"select cours.id_cours, disciplines.nom, profs.nom from disciplines, profs, cours where cours.id_classe in ({id_classe}) and disciplines.id_discipline = cours.id_discipline and profs.id_prof = cours.id_prof"
        cur.execute(requete)
        cours = cur.fetchall()
        self.ui.comboBox_7.clear()
        index = 1
        for cour in cours:
            item = str(cour[0])+ " "+ cour[1]+"  "+ cour[2]
            self.ui.comboBox_7.insertItem(index, item)
            index += 1
        con.close()

    def fill_cours(self):
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        prof = self.ui.comboBox_2.currentText()
        id_profs = f"select id_prof from profs where nom ='{prof}'"
        id_cours = f"select id_cours from cours where id_prof in ({id_profs})"
        description = f"select id_classe, id_discipline from cours where id_cours in ({id_cours})"
        cur.execute(description)
        cours = cur.fetchall()
        self.ui.listWidget_4.clear()
        for cour in cours:
            id_classe = cour[0]
            id_discipline = cour[1]
            cur.execute(f'select Classe from classes where id_classe = {id_classe}')
            classe = cur.fetchall()[0][0]
            cur.execute(f'select nom from disciplines where id_discipline = {id_discipline}')
            discipline = cur.fetchall()[0][0]
            item = discipline + "  "+classe
            self.ui.listWidget_4.addItem(item)
        con.close()

    def fill_disciplines(self):
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        prof = self.ui.comboBox_2.currentText()
        requete = f'SELECT id_prof FROM profs WHERE nom = "{prof}"'
        requete = f'select id_discipline from cours where id_prof in({requete})'
        requete = f'select nom from disciplines where id_discipline in ({requete})'
        cur.execute(requete)
        disciplines = cur.fetchall()
        self.ui.listWidget_2.clear()
        for discipline in disciplines:
            self.ui.listWidget_2.addItem(discipline[0])
        con.close()

    def fill_classes(self):
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        prof = self.ui.comboBox_2.currentText()
        requete = f'SELECT id_prof FROM profs WHERE nom = "{prof}"'
        requete = f'select id_classe from cours where id_prof in({requete})'
        requete = f'select Classe from classes where id_classe in ({requete})'
        cur.execute(requete)
        classes = cur.fetchall()
        self.ui.listWidget_3.clear()
        for classe in classes:
            self.ui.listWidget_3.addItem(classe[0])
        con.close()

    def profs_par_discipline(self):
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        discipline = self.ui.comboBox.currentText()
        print(discipline)
        requete = 'SELECT id_discipline FROM disciplines WHERE nom = "'+discipline+'"'
        print(requete)
        cur.execute(requete)
        resultat = cur.fetchall()
        if resultat:
            id_discipline = resultat[0][0]
        else:
            id_discipline = 0
        requete = f"select id_prof from cours where id_discipline = {id_discipline}"
        requete = f"select nom from profs where id_prof in ({requete})"
        cur.execute(requete)
        resultat = cur.fetchall()
        con.close()
        self.ui.listWidget.clear()
        for prof in resultat:
            self.ui.listWidget.addItem(prof[0])

    def add_discipline(self):
        nom = self.ui.lineEdit.text()
        requete = f"INSERT INTO disciplines (nom) VALUES ('{nom}')"
        con = pymysql.connect('localhost', 'kemar', '', 'projet_notes')
        cur = con.cursor()
        cur.execute(requete)
        cur.execute('select * from disciplines')
        con.commit()
        con.close()
        index = self.ui.comboBox.count()+1
        self.ui.comboBox.insertItem(index, nom)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationIHM()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
