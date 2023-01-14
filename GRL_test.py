import csv

class Dataset:
  def __init__(self, user):
    self.distance = user.get("distance")
    self.time =  user.get("time")
    self.speed = 0
  def set_speed(self,speed):
      self.speed=speed

class UserInput:
    def __init__(self,no_of_user):
        self.users=[]
        for i in range(no_of_user):
            print("Enter details of user ",i+1)
            distance=int(input("Distance (KM): "))
            time=float(input("Time (hrs): "))
            self.users.append({"distance":distance,"time":time})
    def get_users(self):
        return self.users
    
class Measure:
    def measure_speed(self,user_dataset):
        for user_data in user_dataset:
            user_data.speed=user_data.distance/user_data.time

class ShowResults:
    def show_result(self,users_dataset):
        with open('./out.csv', 'w', encoding='UTF8') as f:
          writer = csv.writer(f)
          writer.writerow(["Distance","Time","Speed"])
          print("\nResult >> \nDistance \t Time \t Speed")
          for user_data in users_dataset:
              print(user_data.distance,"KM \t ",user_data.time,"Hrs \t ",user_data.speed,"kmph")
              writer.writerow([user_data.distance,user_data.time,user_data.speed])

          print("\nCSV file exported as out.csv")
            
if __name__ == "__main__":
    users_opj=UserInput(int(input("Enter the number of users: ")))
    users=users_opj.get_users()
    users_dataset=[]
    for user in users:
        users_dataset.append(Dataset(user))
    measure=Measure()
    measure.measure_speed(users_dataset)
    show=ShowResults()
    show.show_result(users_dataset)