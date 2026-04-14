# Práctica: EDA Completo sobre Dataset de E-commerce

## Contexto

Eres junior Data Analyst en una empresa de ecommerce. Tu manager te pide un análisis exploratorio completo de las transacciones del último trimestre (julio-septiembre 2025). El objetivo es entender qué está pasando con las ventas, detectar problemas de datos y extraer insights accionables.

## Dataset

`data/ecommerce_transactions.csv` — ~2.000 transacciones

| Variable | Descripción |
|----------|-------------|
| `order_id` | Identificador de pedido |
| `customer_id` | Identificador de cliente (~500 únicos) |
| `order_date` | Fecha del pedido (julio-sept 2025) |
| `product_category` | electronics / clothing / home / food / beauty |
| `product_name` | Nombre del producto |
| `quantity` | Unidades (⚠️ puede haber errores) |
| `unit_price` | Precio unitario (€) |
| `total_amount` | Importe total (€) |
| `payment_method` | credit_card / debit_card / paypal / bank_transfer |
| `shipping_region` | norte / sur / centro / este / oeste (⚠️ puede haber nulos) |
| `customer_segment` | new / returning / vip |
| `discount_applied` | Descuento aplicado (0-0.3) |
| `returned` | 0 (no devuelto) / 1 (devuelto) |

> ⚠️ El dataset tiene problemas de calidad intencionados. Parte de tu trabajo es encontrarlos.

## Tareas

Completa el notebook `notebook/practica_eda.ipynb` siguiendo el checklist de EDA:

1. **Carga y primera inspección** — shape, dtypes, head, info, describe
2. **Calidad de datos** — Nulos, duplicados, inconsistencias. Documenta todo lo que encuentres
3. **Distribuciones univariantes** — Histogramas para numéricas, value_counts para categóricas
4. **Análisis bivariante y correlaciones** — Scatter plots, groupby, heatmap de correlaciones
5. **Outliers** — Boxplots, criterio IQR o z-score
6. **Hallazgos (mínimo 5)** — Cada uno con título, evidencia (gráfico) e implicación de negocio
7. **Resumen ejecutivo** — Un párrafo para tu manager con las conclusiones clave

## Entrega

- Haz push del notebook completado a `main`
- Tests automáticos + revisión IA se ejecutan al hacer push
- Feedback como comentario en tu commit

## Evaluación

| Criterio | Peso |
|----------|------|
| Detección de problemas de calidad | 25% |
| Visualizaciones adecuadas y variadas | 20% |
| 5+ hallazgos con evidencia y contexto de negocio | 25% |
| Resumen ejecutivo claro | 15% |
| Calidad del código y documentación | 15% |

**Tiempo estimado:** 4-6 horas
