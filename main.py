from sklearn.datasets import load_iris
import pandas as pd
import sys

def load_dataset():
    """
    function reads the dataset 
    """
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df


def dataset_analytics(data_frame):
    """
    function prints the main analytics of a data frame
    parameters: data_frame - the data frame for which the analitics are displayed
    """
    print("Основная информация о датафрейме:")

    print("\nПервые пять элементов датафрейма:")
    print(data_frame.head(5))   
    print("\nИнформация о типах и пропусках:")      
    print(data_frame.info(memory_usage=False))  
    print("\nСтатистические данные:")     
    print(data_frame.describe()) 
    print("\nРазмер датафрейма:")    
    print(f'Количество строк - {data_frame.shape[0]}\nКоличество столбцов - {data_frame.shape[1]}')
       
def main():
    """
    main function of the project
    """
    data_set = load_dataset()
    dataset_analytics(data_set)

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)
