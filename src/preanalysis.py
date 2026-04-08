

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def f_balance_analysis(df, coluna_alvo, plotar=True):
    '''
    Function to analyze the balance of a dataset.
    
    Parameters:
    dataset(pandas):
    column ():
    
    '''
    print("📊 Diagnóstico de Balanceamento")
    print("-" * 40)


    # Frequência absoluta e relativa
    counts = df[coluna_alvo].value_counts()
    proporcoes = df[coluna_alvo].value_counts(normalize=True)

    print("Frequência absoluta:")
    print(counts, "\n")

    print("Frequência relativa (%):")
    print(round(proporcoes * 100, 2), "\n")

    # Razão de desbalanceamento
    maior = counts.max()
    menor = counts.min()
    razao = round(maior / menor, 2)
    
    print(f"🔁 Razão de desbalanceamento (maior/menor): {razao}")

    # Diagnóstico
    # if proporcoes.min() > 0.4:
    #     print("✅ Dataset balanceado.")
    # elif proporcoes.min() > 0.2:
    #     print("⚠️ Ligeiramente desbalanceado.")
    # elif proporcoes.min() > 0.05:
    #     print("🚨 Fortemente desbalanceado!")
    # else:
    #     print("🛑 Severamente desbalanceado!")

    # Diagnóstico
    if razao > 0.4:
        print("✅ Dataset balanceado.")
    elif razao > 0.2:
        print("⚠️ Ligeiramente desbalanceado.")
    elif razao > 0.05:
        print("🚨 Fortemente desbalanceado!")
    else:
        print("🛑 Severamente desbalanceado!")    

    # Sugestões
    if proporcoes.min() < 0.2:
        print("\n🔧 Sugestões para tratamento:")
        print("- Oversampling (ex: SMOTE)")
        print("- Undersampling da classe majoritária")
        print("- Ajustar pesos no modelo (class_weight='balanced')")
        print("- Usar métricas como F1-score ou ROC-AUC")

    # Plot
    if plotar:
        plt.figure(figsize=(6, 4))
        sns.countplot(x=coluna_alvo, data=df)
        plt.title("Distribuição das Classes")
        plt.xlabel("Classe")
        plt.ylabel("Contagem")
        plt.show()



# def f_view_proporcion(dataset, column=None):  
#         ''' Essa função é a principal da página.
# 
#     Parameters:
#     x (int): -
#     y (int): -
# 
#     Returns:
#     int: -.
# 
#     '''
#     if column is None:
#         return dataset.describe()
#     else:
#         return dataset[column].value_counts(normalize=True)
    
    
