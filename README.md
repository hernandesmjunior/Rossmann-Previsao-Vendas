# Rossmann-Previsao-Vendas

<img src="Images/Pharmacy.png">
Ilustração por Glenn Thomas

# PROJETO DE PREVISÃO DE VENDAS - CASO ROSSMANN

Rossmann é uma rede de drogarias com operação em mais de sete países europeus. Vários fatores influenciam o faturamento das lojas, como promoções, presença de concorrentes, feriados estaduais e escolares, sazonalidade e localização. Com dados disponibilizados pela própria Rossmann na plataforma do Kaggle, o objetivo desse projeto é desenvolver um modelo de Machine Learning supervisionado que seja capaz de prever as vendas das próximas seis semanas, e criar uma API para disponibilizá-lo. 

Além do modelo de ML, durante o desenvolvimento do projeto serão utilizadas habilidades como o entendimento do negócio, levantamento e validação de hipóteses, análise descritiva, visualização, tratamento e transformação dos dados.

**Os arquivos utilizados:**

- **train.csv** - historical data including Sales;
- **test.csv** - historical data excluding Sales;
- **sample_submission.csv** - a sample submission file in the correct format;
- **store.csv** - supplemental information about the stores.

**Variáveis presentes nos arquivos:**

A maioria das variáveis possuem nomes auto-explicativos. Aquelas que não possuem:

- **Id** - an Id that represents a (Store, Date) duple within the test set;
- **Store** - a unique Id for each store;
- **Sales** - the turnover for any given day (this is what you are predicting);
- **Customers** - the number of customers on a given day;
- **Open** - an indicator for whether the store was open: 0 = closed, 1 = open;
- **StateHoliday** - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None;
- **SchoolHoliday** - indicates if the (Store, Date) was affected by the closure of public schools;
- **StoreType** - differentiates between 4 different store models: a, b, c, d;
- **Assortment** - describes an assortment level: a = basic, b = extra, c = extended;
- **CompetitionDistance** - distance in meters to the nearest competitor store;
- **CompetitionOpenSince[Month/Year]** - gives the approximate year and month of the time the nearest competitor was opened;
- **Promo** - indicates whether a store is running a promo on that day;
- **Promo2** - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating;
- **Promo2Since[Year/Week]** - describes the year and calendar week when the store started participating in Promo2;
- **PromoInterval** - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store.
