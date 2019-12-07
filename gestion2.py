from lycee2 import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import pymysql
import re

class Singleton():
    def __init__(self, nombre):
        self.nombre = nombre


class ApplicationIHM(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fill_combobox_5()
        self.fill_combobox_7()
        self.fill_combobox_8()
        self.update_note()
        self.fill_combobox()
        self.fill_combobox_2()
        self.fill_combobox_3()
        self.fill_combobox_4()
        self.fill_combobox_10()
        self.fill_combobox_12()
        self.fill_combobox_13()
        self.connect_moyennes()
        self.calcule_moyenne()

    def connect_moyennes(self):
        self.ui.comboBox_10.currentTextChanged['QString'].connect(self.update_eleves)
        self.ui.comboBox_10.currentTextChanged['QString'].connect(self.calcule_moyenne)
        self.ui.comboBox_11.currentTextChanged['QString'].connect(self.calcule_moyenne)
        self.ui.comboBox_13.currentTextChanged['QString'].connect(self.calcule_moyenne)
        self.ui.comboBox_12.currentTextChanged['QString'].connect(self.calcule_moyenne)


    def calcule_moyenne(self):
        classe_text = self.ui.comboBox_10.currentText()
        print("classe_text : ", classe_text)
        discipline_text = self.ui.comboBox_12.currentText()
        print("discipline_txt : ", discipline_text)
        prof_text = self.ui.comboBox_13.currentText()
        print(" prof_txt ", prof_text)
        eleve_text = self.ui.comboBox_11.currentText()
        print("eleve_text : ", eleve_text)
        if not eleve_text:
            return
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        if classe_text == "Toutes":
            liste_id_classes = "SELECT id_classe FROM Classes"
        else:
            id_classe = int(classe_text.split(' ')[0])
            liste_id_classes = f"SELECT id_classe FROM Classes WHERE id_classe = {id_classe}"

        if discipline_text == "Toutes":
            requete = "SELECT id_discipline FROM Disciplines"
            cur.execute(requete)
            liste_disciplines = cur.fetchall()
            liste_id_disciplines = tuple([item[0] for item in liste_disciplines])
        else:
            print(discipline_text)
            id_discipline = int(discipline_text.split(' ')[0])
            liste_id_disciplines = f"({id_discipline})"

        if prof_text == "Tous":
            requete = "SELECT id_prof FROM Profs"
            cur.execute(requete)
            liste_profs = cur.fetchall()
            liste_id_profs = tuple([item[0] for item in liste_profs])
        else:
            print(prof_text)
            id_prof = int(prof_text.split(' ')[0])
            liste_id_profs = f"({id_prof})"

        if eleve_text == "Tous":
            liste_id_eleves = f"SELECT id_eleve FROM Eleves, Classes WHERE Classes.id_classe in ({liste_id_classes})" \
                      f"AND Classes.id_classe = Eleves.id_classe "
        else:
            print('eleve.text : ', eleve_text)
            id_eleve = int(eleve_text.split(' ')[0])
            liste_id_eleves = f"SELECT id_eleve from Eleves WHERE id_eleve = {id_eleve}"
        print(liste_id_eleves)
        cur.execute(liste_id_eleves)
        print(cur.fetchall())
        requete = f"SELECT Notes.Note FROM Notes WHERE Notes.id_eleve in ({liste_id_eleves}) AND " \
                  f"Notes.id_prof in {liste_id_profs} AND Notes.id_discipline in {liste_id_disciplines}"
        print(requete)
        cur.execute(requete)
        liste_notes = cur.fetchall()
        con.close()
        print(liste_notes)
        somme = 0
        n = 0
        for note in liste_notes:
            somme += int(note[0])
            n += 1
        if not n:
            moyenne_str = ''
        else:
            moyenne = somme / n
            moyenne_str = "{0:.2f}".format(moyenne)
        self.ui.lineEdit_4.setText(moyenne_str)


    def fill_combobox_12(self):
        requete = "SELECT id_discipline, Nom FROM Disciplines"
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        cur.execute(requete)
        disciplines = cur.fetchall()
        con.close()
        self.ui.comboBox_12.clear()
        self.ui.comboBox_12.addItem("Toutes")
        for discipline in disciplines:
            item = str(discipline[0]) + ' ' + discipline[1]
            self.ui.comboBox_12.addItem(item)


    def fill_combobox_10(self):
        requete = "SELECT id_classe, Nom FROM Classes"
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        cur.execute(requete)
        classes = cur.fetchall()
        self.ui.comboBox_10.clear()
        self.ui.comboBox_10.addItem("Toutes")
        for classe in classes:
            item = str(classe[0]) + ' ' +classe[1]
            self.ui.comboBox_10.addItem(item)
        self.fill_combobox_11()


    def fill_combobox_13(self):
        requete = "SELECT id_prof, Nom FROM Profs"
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        cur.execute(requete)
        profs = cur.fetchall()
        print(profs)
        self.ui.comboBox_13.clear()
        self.ui.comboBox_13.addItem("Tous")
        for prof in profs:
            item = str(prof[0]) + ' ' + prof[1]
            self.ui.comboBox_13.addItem(item)
        con.close()


    def update_eleves(self):
        self.fill_combobox_11()

    def fill_combobox_11(self):
        classe_text = self.ui.comboBox_10.currentText()
        print("classe text = ", classe_text)
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        if classe_text == "Toutes":
            liste_id_classes = "SELECT id_classe FROM Classes"
        else:
            id_classe = int(classe_text.split(' ')[0])
            liste_id_classes = f"SELECT id_classe FROM Classes WHERE id_classe = {id_classe}"
        requete = f"SELECT id_eleve, Nom, Prenom FROM Eleves WHERE id_classe IN  ({liste_id_classes})"
        print(requete)
        cur.execute(requete)
        eleves = cur.fetchall()
        self.ui.comboBox_11.clear()
        self.ui.comboBox_11.addItem("Tous")
        for eleve in eleves:
            item = str(eleve[0]) + " " + eleve[1] + "  " + eleve[2]
            self.ui.comboBox_11.addItem(item)
        con.close()
        print(self.ui.comboBox_11.currentText())


    def supprime_eleve(self):
        id_eleve = self.get_id_eleve_2()
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        requete1 = f"SELECT id_note FROM  Notes WHERE id_eleve = {id_eleve}"
        cur.execute(requete1)
        liste_id_notes = cur.fetchall()
        print(liste_id_notes)
        if liste_id_notes != ():
            liste_temp = '('
            for note in liste_id_notes:
                liste_temp += str(note[0]) + ','
            liste_finale = liste_temp[:-1] + ')'
            print(liste_finale)
        else:
            liste_finale = '(Null)'
        requete = f"DELETE FROM Notes WHERE id_note in {liste_finale}"
        print(requete)
        cur.execute(requete)
        requete = f"DELETE FROM Eleves WHERE id_eleve = {id_eleve}"
        print(requete)
        cur.execute(requete)
        con.commit()
        con.close()
        self.fill_combobox_6()
        self.fill_combobox_2()


    def get_id_eleve_2(self):
        eleve1 = self.ui.comboBox_2.currentText()
        eleve_split = eleve1.split(' ')
        id_eleve = int(eleve_split[0])
        print(id_eleve)
        return id_eleve


    def ajoute_eleve(self):
        nom_eleve = self.ui.lineEdit_2.text()
        prenom_eleve = self.ui.lineEdit_5.text()
        nom_classe = self.ui.comboBox.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        requete = f"SELECT id_classe FROM  Classes WHERE Nom = '{nom_classe}'"
        cur.execute(requete)
        id_classe = cur.fetchall()[0][0]
        requete = f"INSERT INTO Eleves (Nom, Prenom, id_classe) VALUES ('{nom_eleve}'," \
                  f" '{prenom_eleve}', {id_classe}) "
        cur.execute(requete)
        con.commit()
        con.close()
        self.fill_combobox_2()
        self.fill_combobox_6()
        self.fill_combobox_10()
        self.fill_combobox_12()
        self.fill_combobox_13()
        return None


    def fill_combobox(self):
        requete = "SELECT Nom FROM Classes"
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        cur.execute(requete)
        classes = cur.fetchall()
        self.ui.comboBox.clear()
        for classe in classes:
            self.ui.comboBox.addItem(classe[0])
        con.close()


    def fill_combobox_2(self):
        nom = self.ui.comboBox.currentText()
        id_classe = f"SELECT id_classe FROM Classes WHERE Nom = '{nom}'"
        requete = f"SELECT id_eleve, Nom, Prenom FROM Eleves WHERE id_classe IN ( {id_classe})"
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        cur.execute(requete)
        eleves = cur.fetchall()
        self.ui.comboBox_2.clear()
        for eleve in eleves:
            item = str(eleve[0]) + " " + eleve[1] + "  " + eleve[2]
            self.ui.comboBox_2.addItem(item)
        con.close()


    def fill_combobox_5(self):
        requete = "SELECT Nom FROM Classes"
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        cur.execute(requete)
        classes = cur.fetchall()
        self.ui.comboBox_5.clear()
        for classe in classes:
            self.ui.comboBox_5.addItem(classe[0])
        con.close()


    def fill_combobox_6(self):
        nom = self.ui.comboBox_5.currentText()
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        id_classe = f"SELECT id_classe FROM Classes WHERE Nom = '{nom}'"
        cur.execute(id_classe)
        requete = f"SELECT id_eleve, Nom, Prenom FROM Eleves WHERE id_classe IN ( {id_classe})"
        cur.execute(requete)
        eleves = cur.fetchall()
        self.ui.comboBox_6.clear()
        for eleve in eleves:
            item = str(eleve[0]) + " " + eleve[1] + "  " + eleve[2]
            self.ui.comboBox_6.addItem(item)
        con.close()


    def fill_combobox_3(self):
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        requete = f"select id_prof, Nom from Profs"
        cur.execute(requete)
        profs = cur.fetchall()
        self.ui.comboBox_3.clear()
        for prof in profs:
            item = str(prof[0])+ '  '+ prof[1]
            self.ui.comboBox_3.addItem( item)
        con.close()

    def ajoute_professeur(self):
        prof_nom = self.ui.lineEdit_6.text()
        prof_prenom = self.ui.lineEdit_7.text()
        if prof_nom != '' and prof_prenom != '':
            con = pymysql.connect('localhost', 'kemar', '', 'lycee')
            cur = con.cursor()
            requete = f"INSERT INTO Profs (Nom, Prenom) " \
                      f"VALUES ('{prof_nom}', '{prof_prenom}')"
            cur.execute(requete)
            con.commit()
            con.close()
            self.fill_combobox_3()
            self.fill_combobox_7()
            self.fill_combobox_10()
            self.fill_combobox_12()
            self.fill_combobox_13()

        return None

    def fill_combobox_7(self):
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        requete = f"select Nom from Profs"
        cur.execute(requete)
        profs = cur.fetchall()
        self.ui.comboBox_7.clear()
        for prof in profs:
            self.ui.comboBox_7.addItem( prof[0])
        con.close()


    def fill_combobox_4(self):
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        requete = f"select id_discipline, Nom from Disciplines"
        cur.execute(requete)
        disciplines = cur.fetchall()
        self.ui.comboBox_4.clear()
        for discipline in disciplines:
            id_discipline = discipline[0]
            nom_discipline = discipline[1]
            item = str(id_discipline)+ '  '+ nom_discipline
            self.ui.comboBox_4.addItem( item)
        con.close()

    def ajoute_discipline(self):
        discipline_nom = self.ui.lineEdit_8.text()
        if discipline_nom != '':
            con = pymysql.connect('localhost', 'kemar', '', 'lycee')
            cur = con.cursor()
            requete = f"INSERT INTO Disciplines (Nom) " \
                      f"VALUES ('{discipline_nom}')"
            cur.execute(requete)
            con.commit()
            con.close()
            self.fill_combobox_4()
            self.fill_combobox_8()
        self.fill_combobox_10()
        self.fill_combobox_12()
        self.fill_combobox_13()
        return None

    def fill_combobox_8(self):
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        requete = f"select Nom from Disciplines"
        cur.execute(requete)
        disciplines = cur.fetchall()
        self.ui.comboBox_8.clear()
        for discipline in disciplines:
            self.ui.comboBox_8.addItem( discipline[0])
        con.close()



    def get_notes(self):
        id_eleve = self.get_id_eleve()
        id_prof = self.get_id_prof()
        id_discipline = self.get_id_discipline()
        requete = f"SELECT Note, Date_note, id_note FROM Notes WHERE id_eleve = {id_eleve} AND id_prof = {id_prof}" \
                  f" AND id_discipline = {id_discipline} "
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        cur.execute(requete)
        notes = cur.fetchall()
        return notes

    def update_note(self):
        notes = self.get_notes()
        self.ui.comboBox_14.clear()
        if (notes != ()):
            for note in notes:
                valeur = note[0]
                date = note[1]
                date_affichee =date.strftime('%d/%m/%Y')
                id_note = note[2]
                item = str(valeur) + '     ' + date_affichee + ' ' + str(id_note)
                self.ui.comboBox_14.addItem(item)


    def get_id_eleve(self):
        eleve1 = self.ui.comboBox_6.currentText()
        id_eleve = ''
        for c in eleve1:
            if c == ' ':
                break
            else:
                id_eleve += c
        if id_eleve == '':
            return 0
        return int(id_eleve)

    def change_note(self):
        "Obsolete"
        chaine_note = self.ui.lineEdit_3.text()
        if not chaine_note:
            return
        nouvelle_note = int(chaine_note)
        notes = self.get_notes()
        texte = self.ui.comboBox_9.currentText()
        if not texte:
            return
        texte_split = texte.split('  ')
        id_note = texte_split[1]
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        requete = f"UPDATE Notes SET Note = {nouvelle_note} " \
                  f"WHERE id_note = {id_note}"
        cur.execute(requete)
        con.commit()
        con.close()
        self.update_note()

    def supprime_note(self):
        texte = self.ui.comboBox_14.currentText()
        texte = re.sub(' +', ' ', texte)
        if not texte:
            return
        texte_split = texte.split(' ')
        print("texte : ", texte)
        print(texte_split)
        id_note = texte_split[2]
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        requete = f"DELETE FROM Notes WHERE id_note = {id_note}"
        print(requete)
        cur.execute(requete)
        con.commit()
        con.close()
        self.update_note()

    def ajoute_note(self):
        nouvelle_note = int(self.ui.lineEdit_3.text())
        date_new = self.ui.dateEdit.text()
        date_split = date_new.split('/')
        nouvelle_date = date_split[2]+ ':'+ date_split[1]+ ':'+ date_split[0]
        id_eleve = self.get_id_eleve()
        id_prof = self.get_id_prof()
        id_discipline = self.get_id_discipline()
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        requete = f"INSERT INTO Notes (id_eleve, id_prof," \
                  f"id_discipline, Note, Date_note) VALUES " \
                  f"({id_eleve}, {id_prof}, {id_discipline}," \
                  f" {nouvelle_note}, '{nouvelle_date}')"
        cur.execute(requete)
        con.commit()
        con.close()
        self.update_note()

    def date_changed(self):
        texte = self.ui.comboBox_9.currentText()
        if texte == '':
            return None
        texte_split = texte.split('  ')
        id_note = int(texte_split[1])
        notes = self.get_notes()
        affichage = ''
        for note in notes:
            if note[2] == id_note:
                affichage = str(note[0])
                break
        self.ui.lineEdit_3.setText(affichage)



    def get_id_prof(self):
        nom_prof = self.get_nom_prof()
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        cur.execute(f"SELECT id_prof FROM Profs WHERE Nom = '{nom_prof}'")
        resultat = cur.fetchall()
        if resultat:
            id_prof = resultat[0][0]
        else:
            id_prof = 0
        return id_prof


    def get_nom_prof(self):
        nom_prof = self.ui.comboBox_7.currentText()
        return nom_prof


    def get_id_discipline(self):
        nom_discipline = self.get_nom_discipline()
        con = pymysql.connect('localhost', 'kemar', '', 'lycee')
        cur = con.cursor()
        cur.execute(f"SELECT id_discipline FROM Disciplines WHERE Nom = '{nom_discipline}'")
        resultat = cur.fetchall()
        if resultat:
            id_discipline = resultat[0][0]
        else:
            id_discipline = 0
        return id_discipline


    def get_nom_discipline(self):
        nom_discipline = self.ui.comboBox_8.currentText()
        return nom_discipline


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationIHM()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
