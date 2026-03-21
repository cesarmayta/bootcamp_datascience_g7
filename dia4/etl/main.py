from tasks.extract import extract
from tasks.transform import transform
from tabulate import tabulate

def main():
    data = extract()
    data_transform = transform(data)
    cabeceras = ['nombre','sexo','pais','fecha_nac']
    print(tabulate(data_transform,headers=cabeceras,tablefmt='grid'))
    
if __name__ == "__main__":
    main()