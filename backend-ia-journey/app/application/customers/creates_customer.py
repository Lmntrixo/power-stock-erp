def create_customer(customer_data, repository):
    existing_customer = repository.get_by_email(customer_data.email)
    if existing_customer:
        raise ValueError("cette email est deja utilise")
    return repository.add(customer_data)