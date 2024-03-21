from typing import List

from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    VALID_LOANS = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}
    VALID_CLIENTS = {'Student': Student, 'Adult': Adult}

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.loans: List[StudentLoan, MortgageLoan] = []
        self.clients: List[Student, Adult] = []

    def add_loan(self, loan_type: str):

        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name,client_id,income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):

        client = self.get_client(client_id)
        loan = self.get_loan(loan_type)

        if not client.TYPE == loan.TYPE:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):

        client = self.get_client(client_id)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):

        loans = [l.increase_interest_rate() for l in self.loans if l.TYPE == loan_type]

        return f"Successfully changed {len(loans)} loans."

    def increase_clients_interest(self, min_rate: float):

        client_loans = [c.increase_clients_interest() for c in self.clients if c.interest < min_rate]

        return f"Number of clients affected: {len(client_loans)}."

    def get_statistics(self):

        clients_income = sum([c.income for c in self.clients])
        total_loans_grated = sum([len(c.loans) for c in self.clients if c.loans])
        not_granted_sum = sum([l.amount for l in self.loans])
        avg_interest = sum([i.interest for i in self.clients]) / len(self.clients) if self.clients else 0

        total_sum = 0
        for client in self.clients:
            if client.loans:
                for loan in client.loans:
                    total_sum += loan.amount

        return f"""Active Clients: {len(self.clients)}
Total Income: {clients_income:.2f}
Granted Loans: {total_loans_grated}, Total Sum: {total_sum:.2f}
Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_interest:.2f}"""

    def get_loan(self, loan_type: str):

        loan = [l for l in self.loans if l.TYPE == loan_type]
        return loan[0] if loan else None

    def get_client(self, client_id: str):

        client = [c for c in self.clients if c.client_id == client_id]
        return client[0] if client else None