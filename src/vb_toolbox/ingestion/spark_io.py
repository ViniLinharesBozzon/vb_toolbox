# Preciso algo que pegue seu spark ou pandas dataframe e transforme em arquivo parquet isinstance(v_testeTexto_pd,pd.DataFrame)
# E preciso que faça a camada de delta parquet

def f_set_createSchema(
        p_schema_name: str
) -> None:
    """
    Cria um banco de dados/schema no Spark caso ele não exista.
    
    Args:
        p_schema_name (str): Nome do schema a ser criado.

    Returns:
        None.
    """
    print(f"✅ Criando schema: {p_schema_name} caso não existisse")
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {p_schema_name}")

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


def f_save_dataframe_to_bronze(
     p_dataframe                            # O objeto DataFrame que você já criou
   , p_table_name   : str                   # Nome da tabela (ex: alura_alunos)
   , p_schema_name  : str                   # Nome do Banco de Dados
   , p_catalog_name : str = "bronze"
   , p_mode         : str = "append"        # 'append' (adicionar) ou 'overwrite' (sobrescrever)
):
    """
    Grava um DataFrame da memória para uma Tabela Delta Física (Batch/Job).
    Ideal para cargas manuais ou agendadas (não-streaming).
    """
    
    # Criando o database caso não exista
    f_set_createSchema(p_schema_name)
    
    # Monta o nome final: bronze.alura_alunos
    full_table_name = f"{p_catalog_name}.{p_schema_name}.{p_table_name}"
    
    print(f"--- Iniciando Gravação (Batch) ---")
    print(f"Tabela Alvo: {full_table_name}")
    print(f"Modo: {p_mode.upper()}")
    
    # 2. Configuração da Escrita
    writer = p_dataframe.write.format("delta").mode(p_mode)
    
    # 3. Tratamento de Schema (A mágica da Bronze)
    if p_mode == "append":
        # Se for adicionar, aceita colunas novas que aparecerem (Evolução de Schema)
        writer = writer.option("mergeSchema", "true")
    elif p_mode == "overwrite":
        # Se for sobrescrever, força o novo schema do DataFrame sobre a tabela antiga
        writer = writer.option("overwriteSchema", "true")
        
    # 4. Ação Física (Grava no disco e registra no Metastore)
    writer.saveAsTable(full_table_name)
    
    print(f"--- Sucesso! Dados gravados em {full_table_name} ---")