

class Department(models.Model):
    dept_id = models.CharField(max_length=10, primary_key=True)
    dept_name = models.CharField(max_length=20)
    dept_mgr = models.CharField(max_length=6)

    def __str__(self):
        return self.dept_name
