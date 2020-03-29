from cutecharts.charts import Pie
from cutecharts.faker import Faker


def pie_base() -> Pie:
    chart = Pie("Pie-基本示例")
    chart.set_options(labels=Faker.choose())
    chart.add_series(Faker.values())
    return chart


pie_base().render()