# European_exports_2019_2023
European exports analysis from 2019 to 2023

## Descripción general
Este informe de Power BI titulado "f_exports" proporciona una visualización interactiva de las exportaciones de diferentes categorías de productos, expresadas en valor económico (USD), cantidad medida en toneladas (t) o número de unidades de animales (An) llevadas a cabo durante los años 2019 a 2023 por 40 países europeos.

El objetivo principal es analizar los países con mayor número de exportaciones, identificar los productos más exportados por período o país, detectar tendencias, establecer comparativas y análisis entre diversos países, productos o períodos. Además se han establecido otros indicadores como la esperanza de vida (años), PIB, renta per capita, densidad (hab/km2), población (hab) o la tasa de apertura comercial (Exportaciones / PIB) que refleja el porcentaje exportaciones en relación con la producción interna, para realizar un análisis más profundo por país.

## Fuente de los datos
La principal fuente de datos es https://www.fao.org/faostat/en/#data/TCL donde se ha obtenido el archivo FAOSTAT_data_en_2019_2023.xlsx que junto con el archivo Socioeconomic_Data_2019_2023.xlsx despues de su transformación, limpieza y unión a través de Python constituye la tabla de hechos.

El archivo Socioeconomic_Data_2019_2023.xlsx se ha obtenido con la ayuda de ChatGPT con información de diversas fuentes.

## Transformación y limpieza
En Visual Studio Code se han cargado ambos archivos xlsx. Para unir ambos se ha creado una columna común llamada "Country-Year".
Se han eliminado columnas que no aportaban valor, se ha realizado un análisis de aquellos valores nulos y se han imputado valores faltantes.

Posteriormente, se ha convertido el archivo .json a .py y se ha cargado el script en Power BI Desktop donde se ha continuado con la transformación y limpieza de datos.

Una vez en Power BI Desktop, de la tabla de hechos principal (f_exports_2019_2023) se han obtenido las tablas de dimensiones para las categorías producto (dProducts) y país (dCountry). Se ha generado una tabla de fechas (dDates) y se han creado medidas como por ejemplo Total Exports (USD), Total Exports Quantity (t) y Total Exports Quantity (An) con la función CALCULATE que calcula el valor total de las exportaciones en USD, toneladas y unidades de animales respectivamente.

Asimismo, se han creado otras medidas como Business opening rate = calculate(divide([Total Exports (USD)],[GDP Total SUM])) o tasa de apertura comercial (Exportaciones / PIB), entre otras.

Se ha establecido las relaciones entre la tabla de hechos con las tablas de dimensiones y la tabla de fechas.

## Estructura del informe
El informe está compuesto por las siguientes páginas:

1. **Páginas visibles**
En la página principal aparece el título (European exports 2019 - 2023). En esta página nos encontramos en la parte superior un panel de navegación que nos permitira navegar hasta otras dos páginas que muestran la misma información pero en cantidad (t) y unidades animales (An).

Justo debajo aparecen unos indicadores donde se puede ver el total de las exportaciones en miles de USD, el PIB (DGP) y la tasa de apertura comercial en porcentaje.

Debajo varios gráficos, el primero es un gráfico de barras donde muestra el top 5, es decir los 5 países con mayores exportaciones con barras horizontales. Justo al lado una matriz que se despliega a nivel de país y producto. Debajo un gráfico de líneas donde se muestra la evolución por año y al lado un ranking de los cinco productos más exportados.

Todos estos objetivos visuales pueden ser filtrados por país, año y producto según se interactúe con los filtros a la derecha y justo arriba hay un botón para limpiar todos los filtros.

2. **Páginas no visibles**
En cualquiera de estas tres páginas, si se pincha con el botón derecho en cualquier país podemos acceder a la página llamada "Country Details" donde se puede analizar todas estas otras variables como la población, densidad o esperanza de vida o comparar la evolución en el tiempo de las exportaciones de varios productos en concreto para el país en cuestión.

3. **Consideraciones adicionales**
M = 1.000.000 USD
Bn = 1.000.000.000.000 USD
t = Tonelada (1.000 kg)
An = Animal

## Conclusiones del informe
Analizando los datos en el informe se han pueden obtener varias conclusiones:

- En el período comprendido (2019 - 2023), Holanda es el país con mayor volumen de exportaciones en valor (USD), siendo Francia el pais con mayor volumen de exportaciones en cantidad, principalmente de trigo, seguido muy de cerca por Ucrania que exporta maiz principalmente.
En cuanto a las exportaciones de origen animal es Dinamarca el país que ocupa el primer puesto siendo el cerdo el producto más exportado.

- Si comparamos las exportaciones en USD de tres países, por ejemplo España, Francia y Grecia en el año 2023, podemos ver que el total exportado suma 164.000 millones de USD, situándose Francia en primera posición con 84.000 millones USD, España en segunda posición con 69.000 millones USD y Grecia en tercera posición con 10.000 millones USD. Se puede ver también que el vino es el principal producto exportado con una facturación de 16.000 millones USD, de los cuales corresponden 12.000 millones USD a Francia. 
También podemos destacar que la suma de las exportaciones de estos tres países en el ejercicio 2023 representan un 3,42% de su PIB.

- Si analizamos las exportaciones de aceite de oliva durante los años 2021, 2022 y 2023 podemos observar que han ido aumentando año a año a razón de 1.000 millones de USD cada año, pasando de 7.000 millones aproximadamente en el año 2021 a 9.000 millones en el 2023, alcanzando la cifra total de 25.000 millones USD en esos tres años, siendo España el primer exportador en dicho periodo con 12.000 millones USD.

- En cuanto a productos, en el período comprendido (2019 - 2023) en valor (USD) son las preparaciones alimenticias (frutas y verduras en conserva, produtos de panadería, carnes procesadas) las que ocupan el primer puesto con 189.000 millones USD, seguidas del vino y queso. En cantidad (t) sería el maiz, trigo y cebada en dicho orden, los tres productos más exportados en dicho período.
En unidades de animales (An) sería el cerdo, la oveja y el ganado vacuno en ese orden, siendo el principal exportador Dinamarca.

- Si analizamos por ejemplo las exportaciones de naranjas en el año 2023 vemos que España ocupa el primer puesto en facturación con 1.303 millones USD, seguido por Holanda con 449 millones USD. Sin embargo, si analizamos las exportaciones en cantidad de este producto, vemos que Holanda se coloca en primer lugar con 37 millones de toneladas y España en cuarto lugar con 12,5 millones de toneladas, por lo que se puede concluir que las naranjas españolas son más valoradas y se venden a un precio superior a las holandesas.

- Por último, en España si pinchamos con el botón derecho y analizamos la evolución de dos productos como el vino y aceite de oliva en la página de detalle podemos observar que las exportaciones de aceite de oliva han aumentado de 3.300 millones USD en el año 2019 a 4.500 millones USD en el año 2023. En cambio las exportaciones de vino, aunque no han decrecido, tampoco han aumentado significativamente, pasando de 3.000 millones USD en 2019 a 3.100 millones USD en 2023. Por su parte, Francia, principal exportador de vino, ha pasado de 11.000 millones USD de facturación en 2019 a 13.000 millones USD en 2023, seguida de Italia y España, como segundo y tercer exportador de este producto respectivamente.

  







