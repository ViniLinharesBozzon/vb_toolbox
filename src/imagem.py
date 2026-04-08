# teste de imagens "podres" via tensorflow
# 1- Encontrar a pasta
# 2- Dentro da pasta fazer um laço
# 3- Validar abrir cada imagem para verificar se o Tensorflow vai ter algum problema.

# Problemas
# Path Unico: Test + Treino
# Path Dividido: Teste / Treino
def f_set_image(v_pathImage: str):
    
    from tensorflow.io import read_file,decode_image
    v_fileBytes_tf = read_file(v_pathImage)
    v_fileBytes_tf = decode_image(v_fileBytes_tf, channels=3, expand_animations=False)

def f_get_binImages(
                        v_path_str:        str
                    ,   v_delete_bool:     bool= False
                    ,   v_formatImage_str: str = 'png'
)->tuple[int, list[str]]:
    """
    Docstring for f_get_binImages
    
    :param v_path_str: Path that will search
    :type v_path_str: str
    :param v_delete_bool: If find any image, that i will be deleted?
    :type v_delete_bool: bool
    :param v_formatImage_str: Description
    :type v_formatImage_str: str
    :return: Return the amount of bin imagems and which one is has errors
    :rtype: tuple[int, list[Any]]
    """
    
    import os
    import glob
    print("="*80)
    print("Começando a análise do: ",v_path_str)

    # Usando o formato de imagem solicitado na função
    v_formatImage_str = '*/*.' + v_formatImage_str
    v_path_list       = glob.glob(os.path.join(v_path_str, v_formatImage_str))
   
    v_deletedImages_list: list = []
    v_deleted_int: int = 0

    if v_delete_bool: # Deseja deletar o arquivo
    
        for image in  v_path_list:
            try:
                f_set_image(image)
            except Exception as Error:
                print("A leitura da imagem: ",image,", deu o erro: ",Error)
                v_deletedImages_list.append(image)
                os.remove(image)
                v_deleted_int += 1
                print("-> Deletado 🗑️")
    
    else: # Não deseja deletar o arquivo
    
        for image in  v_path_list:
            try:
                f_set_image(image)
            except Exception as Error:
                print("A leitura da imagem: ",image,", deu o erro: ",Error)
                v_deletedImages_list.append(image)
    
    print("Concluída a análise.")
    print("Imagens análisadas: ", len(v_path_list))
    print("="*80)
    return v_deleted_int , v_deletedImages_list