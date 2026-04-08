import pandas as pd
from typing import Optional

def balance_analysis(df: pd.DataFrame, target_column: str, plot: bool = True) -> Optional[pd.DataFrame]:
    """
    Analisa o balanceamento das classes de um dataset.
    
    Args:
        df (pd.DataFrame): Dataset a ser analisado.
        target_column (str): Nome da coluna alvo (target).
        plot (bool): Se True, exibe o gráfico de distribuição usando Seaborn.
        
    Returns:
        pd.DataFrame: Retorna um dataframe com as contagens se precisar usar depois, 
                      ou None (apenas imprime os resultados).
    """
    print("📊 Diagnóstico de Balanceamento")
    print("-" * 40)

    # Frequência absoluta e relativa
    counts = df[target_column].value_counts()
    proporcoes = df[target_column].value_counts(normalize=True)

    print("Frequência absoluta:")
    print(counts.to_string(), "\n")

    print("Frequência relativa (%):")
    print(round(proporcoes * 100, 2).to_string(), "\n")

    # Razão de desbalanceamento corrigida
    maior = counts.max()
    menor = counts.min()
    
    # Previne divisão por zero se o dataset estiver vazio ou tiver uma classe zerada
    if menor == 0:
        print("🛑 Severamente desbalanceado! A classe minoritária tem 0 registros.")
        return None

    razao = round(maior / menor, 2)
    print(f"🔁 Razão de desbalanceamento (Maior/Menor): {razao}x")

    # Diagnóstico (Lógica Corrigida)
    # Se a razão é 1, é perfeito. Se é 2, a maior tem o dobro da menor, etc.
    if razao <= 1.5:
        print("✅ Dataset balanceado.")
    elif razao <= 4:
        print("⚠️ Ligeiramente desbalanceado.")
    elif razao <= 10:
        print("🚨 Fortemente desbalanceado!")
    else:
        print("🛑 Severamente desbalanceado!")    

    # Sugestões (Usando a proporção da menor classe)
    if proporcoes.min() < 0.2:
        print("\n🔧 Sugestões para tratamento:")
        print("- Oversampling (ex: SMOTE)")
        print("- Undersampling da classe majoritária")
        print("- Ajustar pesos no modelo (class_weight='balanced')")
        print("- Usar métricas robustas (F1-score, ROC-AUC ou PR-AUC)")

    # Plotagem protegida por Lazy Import
    if plot:
        try:
            import matplotlib.pyplot as plt
            import seaborn as sns
            
            plt.figure(figsize=(6, 4))
            # O warning do palette pode ser suprimido definindo hue
            sns.countplot(x=target_column, data=df, hue=target_column, palette="viridis", legend=False)
            plt.title("Distribuição das Classes")
            plt.xlabel("Classe")
            plt.ylabel("Contagem")
            plt.tight_layout()
            plt.show()
        except ImportError:
            print("\n⚠️ Gráfico não gerado: bibliotecas 'matplotlib' e/se 'seaborn' não estão instaladas.")
            print("Para plotar, rode: pip install matplotlib seaborn")

    print("-" * 40)