# Домашнее задание 1
## Корпуса
1. характеристики исследуемого (тематического) корпуса:
Корпус предложений про суды с лемматизацией
	1. Тематика - суд (во всех предложениях присутствует слово "суд")
	2. источник текстов: п.2 https://nlp4year.wikispaces.com/resources
	3. объем корпуса: 1020 предложений, ок. 5100 токенов
	4. параметры предобработки: лемматизированный
2. характеристики контрастного корпуса:
	1. Тематика - новости
	2. источник текстов: п.2 https://nlp4year.wikispaces.com/resources
	3. объем корпуса: 60 тыс предложений, ок. 1 млн 200 тыс токенов
	4. параметры предобработки: лемматизированный, с POS-тэгами

## Таблица
Второй метод - weirdness (формула взята из презентации CL2_2L_KW, слайд 50)

| wi            | Тип        | CountSpecC | CountRefC | LogLikelihood     | Ранг | Weirdness | Ранг |
|---------------|------------|------------|-----------|-------------------|------|-----------|------|
| Top-10        |            |            |           |                   |      |           |      |
| СУД           | тем.       | 1047       | 3816      | 6439.04316145     | 1    | 65.47672  | 19   |
| ПРИЗНАТЬ      | тем.       | 81         | 380       | 462.238251135     | 2    | 50.86863  | 25   |
| УДОВЛЕТВОРИТЬ | тем.       | 56         | 76        | 434.351561462     | 3    | 175.84217 | 4    |
| РЕШЕНИЕ       | тем.       | 93         | 1269      | 350.990271054     | 4    | 17.4892   | 87   |
| АРЕСТ         | тем.       | 53         | 462       | 243.274705536     | 5    | 27.37679  | 57   |
| ИСК           | тем.       | 63         | 880       | 235.091058327     | 6    | 17.08467  | 89   |
| ХОДАТАЙСТВО   | тем.       | 38         | 242       | 196.059532279     | 7    | 37.47286  | 40   |
| ВЫНЕСТИ       | тем.       | 39         | 370       | 172.999128552     | 8    | 25.15426  | 62   |
| ПРИГОВОРИТЬ   | тем.       | 30         | 228       | 145.182120255     | 9    | 31.40039  | 48   |
| ОТКАЗАТЬ      | тем.       | 29         | 220       | 140.438346636     | 10   | 31.45748  | 47   |
|               |            |            |           |                   |      |           |      |
| Anti-top-10   |            |            |           |                   |      |           |      |
| ИДТИ          | общеупотр. | 2          | 483       | 0.000283212994219 | 820  | 0.98817   | 538  |
| ГОСУДАРСТВО   | общеупотр. | 3          | 709       | 0.000281638535441 | 821  | 1.00977   | 530  |
| ПАРТИЯ        | общеупотр. | 5          | 1186      | 0.000182770207079 | 822  | 1.00608   | 531  |
| ЦЕНА          | общеупотр. | 3          | 713       | 5.01344106259e-05 | 823  | 1.00411   | 532  |
| ПРЕМЬЕРА      | общеупотр. | 1          | 240       | 3.20807852485e-05 | 824  | 0.99435   | 537  |
| ОБВИНЯТЬ      | общеупотр. | 2          | 479       | 2.56272452208e-05 | 825  | 0.99642   | 536  |
| СПИСОК        | общеупотр. | 1          | 238       | 7.24116647351e-06 | 826  | 1.0027    | 533  |
| СТАВКА        | общеупотр. | 1          | 238       | 7.24116647351e-06 | 826  | 1.0027    | 533  |
| ВМЕСТЕ        | общеупотр. | 1          | 239       | 2.22707216321e-06 | 827  | 0.99851   | 535  |
| СОГЛАШЕНИЕ    | общеупотр. | 2          | 477       | 7.14832931755e-07 | 828  | 1.0006    | 534  |

Общеупотребительное - условно, употребительное в сфере новостей (контрастный корпус).

В целом, тематические наверху списка, их нет внизу (глагол "обвинять" все-таки не так часто используют в контексте судебных решений), а не-судебных нет наверху, так что LogLikelihood сработал хорошо. В целом, weirdness тоже соответствует - в смысле высоких позиций топа-10 и низких анти-топа-10, но более детально weirdness не сходится с LogLikelihood.

Вместо ручного выбора просто топ-10 слов по частоте: <br>
СУД РЕШЕНИЕ ПРИЗНАТЬ ИСК ДЕЛО УДОВЛЕТВОРИТЬ АРЕСТ ВЫНЕСТИ ХОДАТАЙСТВО ГОД <br> 
* точность (процент слов в списке по log likelihood, которые есть в этом списке) - 80%
* полнота (процент слов из этого списка, которые есть в списке по log likelihood) - 80%
