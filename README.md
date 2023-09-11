Funcionamento da API
A API aceita solicitações HTTP POST contendo dados do cliente em formato JSON e retorna a previsão da pontuação de gastos para esse cliente. Os dados do cliente devem incluir "Gender" (gênero), "Age" (idade) e "AnnualIncome" (renda anual). A previsão é retornada no formato JSON, incluindo a chave "SpendingScorePrediction".

Exemplo de solicitação:

json
Copy code
{
    "Gender": "Male",
    "Age": 30,
    "AnnualIncome": 50000
}
Exemplo de resposta:

json
Copy code
{
    "Gender": "Male",
    "Age": 30,
    "AnnualIncome": 50000,
    "SpendingScorePrediction": 65.2
}
Modelo de Machine Learning
Foi escolhido um modelo de regressão linear para prever a pontuação de gastos de um cliente. A escolha desse modelo foi baseada em testes comparativos com outros modelos, como árvores de decisão e regressão logística. O modelo de regressão linear apresentou um desempenho satisfatório e é relativamente simples de entender e implementar. Além disso, ele fornece uma previsão numérica, o que é adequado para esse problema de regressão.

Instruções para Executar a Aplicação
Para executar a aplicação, siga os passos abaixo:

Certifique-se de ter o Python 3.9 instalado em seu ambiente.

 docker build -t customer-segmentation-app .
 docker run -d -p 8000:8000 customer-segmentation-app


A API estará disponível em http://localhost:8000/predict/ . Você pode fazer solicitações POST para esta URL para obter previsões de pontuação de gastos.

Treinamento do Modelo
O treinamento do modelo é realizado manualmente antes inicialização da aplicação. Os dados de treinamento são carregados a partir do arquivo "dados_codificados.csv" e usados para treinar o modelo de regressão linear no arquivo model.py.

Pré-processamento dos Dados
Antes do treinamento, os dados são pré-processados para garantir que estejam prontos para alimentar o modelo. Isso inclui a codificação do gênero (0 para "Male" e 1 para "Female") e a remocao da coluna de ID.