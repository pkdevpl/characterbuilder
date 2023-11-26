# Todo

* user - dodawanie nowego usera po przesłaniu formularza
* user - logowanie


* formularz dodawania nowej postaci
  * nowy template form.html - uzupełnić z bootstrapem
  * podpiąć template w character/views.py
  * dodać zabezpieczenie niezalogowanych userów w views.py na zasadzie users/views.py
  * dodać formularz bootstrapowy na zasadzie register user
* formularz edycji
* strona detali postaci
* dodać modele 
  * Quest
    * name = resque mission, protect, collect resources
    * description = 
  * UserQuest
    * user.ForeignKey
    * quest.ForeignKey
* naprawić formularz dodawania postaci - zbliżone do rejestracji użytkownika

* https://getbootstrap.com/docs/5.3/components/buttons/

```shell
git clone https://github.com/pkdevpl/characterbuilder.git
```

## 26.11.2023

* Pierwszy widok powinien pokazywać listę postaci i liczbę golda
* User na początku powinien nie mieć żadnej postaci i utworzyć jedną przez formularz
* Utworzenie postaci powinno zmniejszyć liczbę golda w {{party.gold}} np. o 1000
* Jeżeli nie ma 1000 golda, przycisk tworzenia postaci powinien być wyłączony
* Na liście postaci powinien być widok ilości golda {{party.gold}}
* Każda postać na liście powinna mieć przycisk Wybierz zadanie/quest
* Przycisk Wybierz quest, powinien przekierować do listy questów

* Na liście questów powinna być nazwa postaci, jej level i exp
* Na liście powinny być tylko questy, których level <= character.getLevel i quest.status != 'completed' 
* Na liście każdy quest powinien mieć nazwę, podany czas, exp i gold i przycisk Rozpocznij, 
* Po kliknięciu Rozpocznij, tworzony jest model CharacterQuest przypisany do Character
* Inne questy powinny być niedostępne (przycisk Rozpocznij disabled albo nie wyświetlony)
* Fajnie, jeśli będzie timer odliczający czas do ukończenia questu
* Po zakończeniu questu, liczba gold w Party.gold powinna zostać powiększona o quest.gold (zarobiony na queście)
* Po zakończeniu questu, liczba exp u Character powinna być powiększona o quest.exp

* Za zarobiony gold, można stworzyć nową postać
* Kolejne postaci mogą robić inne questy i też zarabiać golda

* rzeczy jak Questy, Skille, Profesje można zdefiniować dodając /admin na końcu

Widoki:
* lista postaci
* dodaj postać
  * w formularzu pole wyboru profesji
  * pole wyboru rasy

* lista questów