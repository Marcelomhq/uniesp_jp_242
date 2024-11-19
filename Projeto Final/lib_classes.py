class Slip:
    def __init__(self,slip_id,advice):
        self.id = slip_id
        self.advice = advice
    
    def to_dict(self):
        return {"id": self.id, "advice": self.advice}
    
    def __repr__(self):
        return f'ID: {self.id}, Advice: {self.advice}'
    

if __name__ == "__main__":
    slip = Slip(1, "Test advice")
    # print(slip.to_dict())
    print(slip)