App classroom

  Model Student
    name  => CharField(10)
    phone => CharField(20)
    is_cs => BooleanField()
    age   => IntegerField()

  ModelForm StudentForm
    ??

  Views => Create, Read, Update, Delete

  URL
    URL             => view function name
    /classroom/     => index
    /classroom/1/   => detail
    /classroom/new/ => create




