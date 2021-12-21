from car.models import Car

def get_object(self):
    get_category = self.request.query_params.get('category')
    if get_category==None:
        return Car.objects.all()
    return Car.objects.filter(category=get_category)
