# Company Clust
Разработать решение для кластеризации названий компаний по идентичности обозначаемой компании.

## Подход 1: классификатор SKLearn

## Подход 2: кластеризатор SKLearn

## Подход 3: эмбеддинги текста
Language-agnostic BERT Sentence Embedding (LaBSE)
- С помощью LaBSE извлекаем вектора признаков (эмбеддинги) предложений с помощью модели LaBSE
- Извлекаем меры схожести пар векторов (пар названий компаний) - евклидово и косинусное расстояния <br>
![img_1.png](misc/img_1.png) 
![img.png](misc/img.png) <br>

## Эксперименты с косинусным расстоянием:<br>
Обучение классификатора случайный лес RandomForest<br>
![img_9.png](misc/img_9.png)<br>
Обучение классификатора логистическая регрессия LogisticRegression<br>
![img_10.png](misc/img_10.png)<br>
Обучение и оптимизация гиперпараметров классификатора случайный лес<br>
![img_11.png](misc/img_11.png)<br>
Upsamling данных, обучение RandomForest<br>
![img_4.png](misc/img_4.png)<br> 
![img_5.png](misc/img_5.png)<br>

Upsamling данных, обучение LogisticRegression<br>
![img_6.png](misc/img_6.png)<br>
Upsampling данных, обучение и оптимизация гиперпараметров RandomForest<br>
![img_7.png](misc/img_7.png)<br>
## Эксперименты с евклидовым расстоянием:<br>
Обучение классификатора случайный лес RandomForest<br>
![img_2.png](misc/img_2.png)<br>
Обучение классификатора логистическая регрессия LogisticRegression<br>
![img_3.png](misc/img_3.png)<br>
Обучение и оптимизация гиперпараметров классификатора случайный лес<br>
![img_8.png](misc/img_8.png)<br>