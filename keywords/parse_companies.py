import re
useless_words = ['Inc', 'Corporation', 'Company', 'Corp', 'Co', 'Energy', '&', 'The', '.com', "Inc.", "Corp.", "Co.", "of", "Ltd.", "Ltd"]


with open('companies.txt', 'r') as f:
    companies = f.readlines()

new_companies = []
for company in companies:
    company = company[:-1]
    company_words = company.split()
    new_company = [word for word in company_words if word not in useless_words]
    new_companies.append([word.lower() for word in new_company])
    

print new_companies
with open('parsed_companies.txt', 'w') as f:
    for company in new_companies:
        f.write(' '.join(company)+'\n')
