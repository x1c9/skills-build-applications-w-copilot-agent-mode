from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='password1')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='password2')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='password3')

        # Create teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.set([user1, user2])
        team2 = Team.objects.create(name='Team Beta')
        team2.members.set([user3])

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_points=5)
        workout2 = Workout.objects.create(name='Running', description='Run 1 mile', suggested_points=10)

        # Create activities
        Activity.objects.create(user=user1, activity_type='Pushups', duration=10, points=5)
        Activity.objects.create(user=user2, activity_type='Running', duration=20, points=10)
        Activity.objects.create(user=user3, activity_type='Pushups', duration=15, points=5)

        # Create leaderboard
        Leaderboard.objects.create(team=team1, total_points=15)
        Leaderboard.objects.create(team=team2, total_points=5)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
