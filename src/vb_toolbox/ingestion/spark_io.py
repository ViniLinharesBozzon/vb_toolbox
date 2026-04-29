# Preciso algo que pegue seu spark ou pandas dataframe e transforme em arquivo parquet isinstance(v_testeTexto_pd,pd.DataFrame)
# E preciso que faça a camada de delta parquet

def f_set_createDatabase(
        p_schema_name: str
) -> None:
    """
    Cria um banco de dados/schema no Spark caso ele não exista.
    
    Args:
        p_schema_name (str): Nome do schema a ser criado.

    Returns:
        None.
    """
    print(f"✅ Criando database: {p_schema_name} caso não existisse")
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {p_schema_name}")

    return None

def f_set_dataframe2Parquet(
    p_dataframe
 ,  p_pathTarget    : str
 ,  p_uniqueFile    : bool = True
 ) -> None:
    """
    Args:
    p_dataframe: Dataframe Spark que será exportado
    p_pathTarget (str): Caminho do arquivo que será exportado.        
    p_uniqueFile (bool): Usado para export de arquivo único.

    Returns:
        None.
    """
    if p_uniqueFile: # Salva em arquivo único seu dataframe
        p_dataframe.coalesce(1).write.mode("overwrite").parquet(p_pathTarget)
    else:
        raise ValueError("❌ Exportação sem ser via arquivo único ainda não desenvolvido. Favor alterar o parametro: p_uniqueFile")
    return None