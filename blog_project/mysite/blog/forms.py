from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(PostForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['lname'].required = False
        self.fields['job'].required = False
        self.fields['organ'].required = False
        self.fields['q1'].required = False
        self.fields['q2'].required = False
        self.fields['q3'].required = False
        self.fields['q4'].required = False
        self.fields['q5'].required = False
        self.fields['q6'].required = False
        self.fields['q7'].required = False
        self.fields['q8'].required = False
        self.fields['q9'].required = False
        self.fields['q10'].required = False
        self.fields['q11'].required = False
        self.fields['q12'].required = False


    class Meta():
        model = Post
        fields = ('name','lname','city','job','organ','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12')
        labels = {'name': ('First Name') ,'lname': ('Last Name') ,'city': ('City'),'job': ('Job/Student'),'organ': ('Organisation/University'),
                   'q1': ('If you could break any world record which one would it be during this lockdown?'),
                   'q2': ('What’s a story – from a book, a movie, an article, a conversation – that you’ve been gripped by recently? Why did it capture you?'),
                   'q3': ('What will be your New Normal Post Quarantine ?'),
                   'q4': ('Coffee or Tea?'),
                   'q5': ('What would the title of your Autobiography be?'),
                   'q6': ('What would be the most surprising scientific discovery imaginable ?'),
                   'q7': ('Describe your Quarantine with a Movie Name or Rewrite movie titles so they would follow quarantine regulations.'),
                   'q8': ('Do you think the situation is acting as a social leveller, or making inequalities more apparent? Is  this Social distancing bringing us together since we are all fighting a common enemy ?'),
                   'q9': ('If you could write a letter to yourself in future , what would you say?'),
                   'q10': ('What do you hope we all learn or take away from this experience?'),
                   'q11': ('What keeps you motivated during tough times ? As a leader How would you motivate people around you ?'),
                   'q12': ('What is your Philosophy of Life for the world as an inspirational quote ?')}



        widgets = {
         'job':forms.TextInput(attrs={'placeholder': 'Job Role or Field of Study as a Student','class':'textinputclass'}),
         'q1':forms.Textarea(attrs={'placeholder': '#Sleeping','rows': 2,'class':' postcontent'}),
         'q2':forms.Textarea(attrs={'rows': 3,'class':' postcontent'}),
         'q3':forms.Textarea(attrs={'placeholder': '#Namaste for Greetings','rows': 1}),
         'q5':forms.Textarea(attrs={'placeholder': '#Around the World in 80 Semesters','rows': 1}),
         'q6':forms.Textarea(attrs={'placeholder': '#Time Travel','rows': 2,'class':' postcontent'}),
         'q7':forms.Textarea(attrs={'placeholder': '#Harry Potter and the Semester he finished online #Harry Potter and the chamber of isolation #Don   t Stand by me','rows': 2,'class':' postcontent'}),
         'q8':forms.Textarea(attrs={'rows': 3,'class':' postcontent'}),
         'q9':forms.Textarea(attrs={'rows': 2,'class':' postcontent'}),
         'q10':forms.Textarea(attrs={'rows': 3,'class':' postcontent'}),
         'q11':forms.Textarea(attrs={'rows': 3,'class':' postcontent'}),

        }
