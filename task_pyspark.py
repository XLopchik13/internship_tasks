from pyspark.sql import SparkSession


def return_pairs(products, categories):
    df_joined = products.join(categories, "product_id", "left_outer")

    pairs = df_joined.select("product_name", "category_name")

    uncategorized = df_joined.filter(df_joined.category_name.isNull())
    uncategorized = uncategorized.select("product_name")

    return pairs, uncategorized


if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("ProductCategory") \
        .master("local[*]") \
        .getOrCreate()

    products_data = [(1, "product1"),
                     (2, "product2"),
                     (3, "product3")]

    categories_data = [(1, "category1", 1),
                       (2, "category2", 1),
                       (3, "category3", 2)]

    df_products = spark.createDataFrame(products_data, ["product_id", "product_name"])
    df_categories = spark.createDataFrame(categories_data, ["category_id", "category_name", "product_id"])

    df_pairs, df_uncategorized = return_pairs(df_products, df_categories)

    print("Product-Category pairs:")
    df_pairs.show()

    print("Uncategorized Products:")
    df_uncategorized.show()

    spark.stop()
