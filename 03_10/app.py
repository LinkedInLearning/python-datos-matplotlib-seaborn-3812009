import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage,AnnotationBbox

df_ventas = pd.DataFrame({
    'cromos': ['Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102'],
    'ventas': [100, 150, 200, 123, 258, 156, 369, 212]
  })

fig, ax = plt.subplots()

grupo_cromos_df = df_ventas.groupby('cromos')['ventas'].sum()
ax.bar(range(len(grupo_cromos_df)), 
       grupo_cromos_df, 
       tick_label=grupo_cromos_df.index,
       color=['khaki', 'plum'])
ax.set_ylabel('Venta (Dólares)')
ax.set_xlabel('Cromos')
ax.set_title('Venta en dólares de cromos del 2023', fontsize=16, color='green', fontweight='bold', ha='center', pad=20)

zoom=0.08

for index, cromo in enumerate(grupo_cromos_df.index):
    imagen_cromo = plt.imread(f"images/{index+1}.png")
    im = OffsetImage(imagen_cromo, zoom)
    im.image.axes = ax

    annotation_bbox = AnnotationBbox(im, (index, 0),  xybox=(0, -40), frameon=False, boxcoords="offset points")
    ax.add_artist(annotation_bbox)

plt.subplots_adjust(bottom=0.2)
plt.show()
