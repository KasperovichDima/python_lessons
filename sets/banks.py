# Создадим несколько банков
# JPM = 'JPMorgan Chase'
# BOFA = 'Bank of America'
# CTGR = 'Citigroup'
# WFC = 'Wells Fargo & Co.'
# USB = 'U.S. Bancorp'
# PNC = 'PNC Financial Services'
# TFC = 'Truist Financial Corporation'
# GSS = 'Goldman Sachs'
# TDB = 'TD Bank'
# CPO = 'Capital One'

# Банки с лицензией:
has_license: set[str] = {'JPM', 'CTGR', 'WFC', 'PNC', 'TFC', 'CPO'}
# Банки, у которых есть мобильное приложение:
has_mobile_app: set[str] = {'BOFA', 'CTGR', 'USB', 'TFC', 'GSS'}
# Банки, которые работают в международной системе SWIFT:
support_swift: set[str] = {'JPM', 'CTGR', 'WFC', 'PNC', 'TFC', 'GSS', 'TDB'}
# Банки, которые имеют офисы за пределами США:
international: set[str] = {'JPM', 'BOFA', 'USB', 'GSS', 'CPO'}
