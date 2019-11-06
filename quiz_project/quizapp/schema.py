import graphene

from graphene import relay, ObjectType, Connection, Node, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django_filters import FilterSet, OrderingFilter
from django.contrib.auth.models import User


from .models import *

# Graphene will automatically map the Article model's fields onto the ArticleNode.
# This is configured in the ArticleNode's Meta class (as you can see below)
class ExtendedConnection(Connection):
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length
    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)



# class TimemodelsNode(DjangoObjectType):
#     class Meta:
#         model = Timemodels
#         filter_fields = ['date_add', 'date_update','statut']
   
      
#         interfaces = (relay.Node, )
#         connection_class = ExtendedConnection

class LevelNode(DjangoObjectType):
    class Meta:
        model = Level
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'description':['exact','icontains', 'istartswith'],
            
        }
        interfaces = (relay.Node, )


class QuizNode(DjangoObjectType):
    class Meta:
        model = Quiz
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'max_question':['exact'],
            'correction': ['exact',],
            'level': ['exact'],
            'single_tentative': ['exact'],
            'result_tentative': ['exact'],
            'pourcentage_requis': ['exact'],
            'success_text': ['exact', 'icontains', 'istartswith'],
            'fail_text': ['exact', 'icontains', 'istartswith'],


        }
        order_by = OrderingFilter(
            fields=(
                ('date_add','date_add'),
            )
        )
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection






class Image_testNode(DjangoObjectType):
    class Meta:
        model = Image_test
        # Allow for some more advanced filtering here
        filter_fields = {
            'date_update':['exact',],
            'date_add':['exact',],
            'statut':['exact',],


          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        # Allow for some more advanced filtering here
        filter_fields = {
            'contenu': ['exact', 'icontains', 'istartswith'],
            'quiz':['exact',],
            'level':['exact',],
            # 'image_question':['exact',],
            'description': ['exact', 'icontains', 'istartswith'],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection

class ReponseNode(DjangoObjectType):
    class Meta:
        model = Reponse
        filter_fields = {
            'reponse': ['exact', 'icontains', 'istartswith'],
            'score':['exact',],
            'question':['exact',],
            # 'image_question':['exact',],
            'description': ['exact', 'icontains', 'istartswith'],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection

class ResultatNode(DjangoObjectType):
    class Meta:
        model = Resultat
        filter_fields = {
            'quiz_id':['exact',],
            'user_id':['exact',],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection



# class ArticleType(DjangoObjectType):
#     class Meta:
#         model = Article
# class CommentaitreType(DjangoObjectType):
#     class Meta:
#         model = Commentaire
# # ...code
# # Change the CreateLink mutation
# class ArticleInput(graphene.InputObjectType):
#     titre = graphene.String()
# class CommentaireInput(graphene.InputObjectType):
#     article_id = graphene.Field(ArticleInput)
#     contenu = graphene.String()


# class CreateCommentaire(graphene.Mutation):
#     commentaitre = graphene.Field(CommentaitreType)
 

  



#     class Arguments:
#         commentaire_data = CommentaireInput(required=True)
      

#     @staticmethod
#     def mutate(root, info, commentaire_data , article_id    ):
#         user = info.context.user or None
#         commentaire = Commentaire.objects.create(**commentaire_data,username=user )
#         return CreateCommentaire(commentaitre=commentaitre)
   

class Query(ObjectType):
    # Timemodels = relay.Node.Field(TimemodelsNode)
    # all_Timemodels = DjangoFilterConnectionField(TimemodelsNode)
    
    Level = relay.Node.Field(LevelNode)
    all_Levels = DjangoFilterConnectionField(LevelNode)

    Quiz = relay.Node.Field(QuizNode)
    all_Quizs = DjangoFilterConnectionField(QuizNode)

    Image_test = relay.Node.Field(Image_testNode)
    all_Image_tests = DjangoFilterConnectionField(Image_testNode)


    Question = relay.Node.Field(QuestionNode)
    all_Questions = DjangoFilterConnectionField(QuestionNode)
    
    Reponse = relay.Node.Field(ReponseNode)
    all_Reponse = DjangoFilterConnectionField(ReponseNode)
    
    Resultat = relay.Node.Field(ResultatNode)
    all_Resultat = DjangoFilterConnectionField(ResultatNode)

    
# class Mutation(graphene.ObjectType):
        
#     create_CreateCommentaire = CreateCommentaire.Field()
   
# -------------------------------------------------------------------

# Create Input Object Types
class LevelInput(graphene.InputObjectType):
    id = graphene.ID()
    nom = graphene.String()
    description = graphene.String()

class QuizInput(graphene.InputObjectType):
    id = graphene.ID()
    titre = graphene.String()
    description = graphene.String()
    level = graphene.Field(LevelInput)
    max_question = graphene.Int()
    correction = graphene.String()
    single_tentative = graphene.String()
    result_tentative = graphene.String()
    pourcentage_requis = graphene.Int()
    success_text = graphene.String()
    fail_text = graphene.String()

class Image_testInput(graphene.InputObjectType):
    id = graphene.ID()
    image = graphene.String()

class QuestionInput(graphene.InputObjectType):
    id = graphene.ID()
    quiz = graphene.List(QuizInput)
    level = graphene.Field(LevelInput)
    description = graphene.String()
    contenu = graphene.String()
    image_question = graphene.List(Image_testInput)

class ReponseInput(graphene.InputObjectType):
    id = graphene.ID()
    description = graphene.String()
    score = graphene.Int()
    image_reponse = graphene.List(Image_testInput)
    question = graphene.Field(QuizInput)

    

# Create mutations for Level
class CreateLevel(graphene.Mutation):
    class Arguments:
        input = LevelInput(required=True)

    ok = graphene.Boolean()
    level = graphene.Field(LevelNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        level_instance = Level(nom=input.nom, description=input.description)
        level_instance.save()
        return CreateActor(ok=ok, level=level_instance)

class UpdateLevel(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = LevelInput(required=True)

    ok = graphene.Boolean()
    level = graphene.Field(LevelNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        level_instance = Level.objects.get(pk=id)
        if level_instance:
            ok = True
            level_instance.nom = input.nom
            level_instance.description = input.description
            level_instance.save()
            return UpdateLevel(ok=ok, actor=level_instance)
        return UpdateLevel(ok=ok, level=None)


# Create mutations for Quiz
class CreateQuiz(graphene.Mutation):
    class Arguments:
        input = QuizInput(required=True)

    ok = graphene.Boolean()
    quiz = graphene.Field(QuizNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        levels = []
        for level_input in input.level:
          level = Level.objects.get(pk=level_input.id)
          if level is None:
            return CreateQuiz(ok=False, quiz=None)
          levels.append(level)
        quiz_instance = Quiz(
          titre=input.titre,
          description=input.description,
          level=input.level,
          max_question=input.max_question,
          correction=input.correction,
          single_tentative=input.single_tentative,
          result_tentative=input.result_tentative,
          pourcentage_requis=input.pourcentage_requis,
          success_text=input.success_text,
          fail_text=input.fail_text
          )
        quiz_instance.save()
        quiz_instance.level.set(levels)
        return CreateQuiz(ok=ok, quiz=quiz_instance)


class UpdateQuiz(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = QuizInput(required=True)

    ok = graphene.Boolean()
    quiz = graphene.Field(QuizNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        quiz_instance = Movie.objects.get(pk=id)
        if quiz_instance:
            ok = True
            levels = []
            for level_input in input.level:
              level = Level.objects.get(pk=level_input.id)
              if level is None:
                return UpdateQuiz(ok=False, quiz=None)
              levels.append(level)
            quiz_instance.titre=input.titre
            quiz_instance.description=input.description
            quiz_instance.max_question=input.max_question
            quiz_instance.correction=input.correction
            quiz_instance.single_tentative=input.single_tentative
            quiz_instance.result_tentative=input.result_tentative
            quiz_instance.pourcentage_requis=input.pourcentage_requis
            quiz_instance.success_text=input.success_text
            quiz_instance.fail_text=input.fail_text
            quiz_instance.level.set(levels)
            return UpdateQuiz(ok=ok, quiz=quiz_instance)
        return UpdateQuiz(ok=ok, quiez=None)

# Create mutations for Image_test
class CreateImage_test(graphene.Mutation):
    class Arguments:
        input = Image_testInput(required=True)

    ok = graphene.Boolean()
    image_test = graphene.Field(Image_testNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        image_teste_instance = Image_test(image=input.image)
        image_teste_instance.save()
        return CreateImage(ok=ok, image_test=image_teste_instance)

class UpdateImage_test(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = Image_testInput(required=True)

    ok = graphene.Boolean()
    image_test = graphene.Field(Image_testNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        image_test_instance = Actor.objects.get(pk=id)
        if image_test_instance:
            ok = True
            image_test_instance.image = input.image
            image_test_instance.save()
            return UpdateImage_test(ok=ok, image_test=image_test_instance)
        return UpdateImage_test(ok=ok, image_test=None)

# Create mutations for Question
class CreateQuestion(graphene.Mutation):
    class Arguments:
        input = QuestionInput(required=True)

    ok = graphene.Boolean()
    question = graphene.Field(QuestionNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        # quiz elements
        quizs = []
        for quiz_input in input.quiz:
          quiz = Quiz.objects.get(pk=quiz_input.id)
          if quiz is None:
            return CreateQuestion(ok=False, question=None)
          quizs.append(quiz)

        # Level elements
        levels = []
        for level_input in input.level:
          level = Level.objects.get(pk=level_input.id)
          if level is None:
            return CreateQuestion(ok=False, question=None)
          levels.append(level)

        # image_question elements
        image_questions = []
        for image_question_input in input.image_question:
          image_question = Image_test.objects.get(pk=image_question_input.id)
          if image_question is None:
            return CreateQuiz(ok=False, question=None)
          image_questions.append(image_question)

    
        question_instance = Question(
          description=input.description,
          contenu=input.contenu
          )
        question_instance.save()
        question_instance.quiz.set(quizs)
        question_instance.level.set(levels)
        question_instance.image_question.set(image_questions)
        return CreateQuestion(ok=ok, movie=question_instance)


class UpdateQuestion(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = QuestionInput(required=True)

    ok = graphene.Boolean()
    question = graphene.Field(QuestionNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        question_instance = Question.objects.get(pk=id)
        if question_instance:
            ok = True

            # quiz elements
            quizs = []
            for quiz_input in input.quiz:
                quiz = Quiz.objects.get(pk=quiz_input.id)
                if quiz is None:
                    return CreateQuestion(ok=False, question=None)
                quizs.append(quiz)

            # Level elements
            levels = []
            for level_input in input.level:
                level = Level.objects.get(pk=level_input.id)
                if level is None:
                    return CreateQuestion(ok=False, question=None)
                levels.append(level)

            # image_question elements
            image_questions = []
            for image_question_input in input.image_question:
                image_question = Image_test.objects.get(pk=image_question_input.id)
                if image_question is None:
                    return CreateQuiz(ok=False, question=None)
                image_questions.append(image_question)


            question_instance.description=input.description
            question_instance.contenu=input.contenu
            question_instance.quiz.set(quizs)
            question_instance.level.set(levels)
            question_instance.image_question.set(image_questions)
            return UpdateQuestion(ok=ok, question=question_instance)
        return UpdateQuestion(ok=ok, question=None)


# Create mutations for Reponse
class CreateReponse(graphene.Mutation):
    class Arguments:
        input = ReponseInput(required=True)

    ok = graphene.Boolean()
    reponse = graphene.Field(ReponseNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True

        image_reponses = []
        for image_reponse_input in input.image_reponse:
          image_reponse = Image_test.objects.get(pk=image_reponse_input.id)
          if image_reponse is None:
            return CreateReponse(ok=False, reponse=None)
          image_reponses.append(image_reponse)

        questions = []
        for question_input in input.question:
          question = Question.objects.get(pk=question_input.id)
          if question is None:
            return CreateReponse(ok=False, reponse=None)
          questions.append(question)

        reponse_instance = Reponse(
          description=input.description,
          reponse=input.reponse,
          score=input.score
          )
        reponse_instance.save()
        reponse_instance.image_reponse.set(image_reponses)
        reponse_instance.question.set(questions)
        return CreateReponse(ok=ok, reponse=reponse_instance)


class UpdateReponse(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ReponseInput(required=True)

    ok = graphene.Boolean()
    reponse = graphene.Field(ReponseNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        reponse_instance = Reponse.objects.get(pk=id)
        if reponse_instance:
            ok = True
            image_reponses = []
            for image_reponse_input in input.image_reponse:
                image_reponse = Image_test.objects.get(pk=image_reponse_input.id)
                if image_reponse is None:
                    return CreateReponse(ok=False, reponse=None)
                image_reponses.append(image_reponse)

            questions = []
            for question_input in input.question:
                question = Question.objects.get(pk=question_input.id)
                if question is None:
                    return CreateReponse(ok=False, reponse=None)
                questions.append(question)

            reponse_instance.description=input.description
            reponse_instance.reponse=input.reponse
            reponse_instance.score=input.score
            reponse_instance.image_reponse.set(image_reponses)
            reponse_instance.question.set(questions)
            return UpdateReponse(ok=ok, reponse=reponse_instance)
        return UpdateReponse(ok=ok, reponse=None)
    

class Mutation(graphene.ObjectType):
    create_level = CreateLevel.Field()
    update_level = UpdateLevel.Field()

    create_quiz = CreateQuiz.Field()
    update_quiz = UpdateQuiz.Field()

    create_image_test = CreateImage_test.Field()
    update_image_test = UpdateImage_test.Field()

    create_question = CreateQuestion.Field()
    update_question = UpdateQuestion.Field()

    create_reponse = CreateReponse.Field()
    update_reponse = UpdateReponse.Field()


