import json
import os
from datetime import date

import click

PROFILE_PATH = os.path.join('fitness-journal', 'fitness_data', 'profile.json')
WORKOUT_PATH = os.path.join('fitness-journal', 'fitness_data', 'workouts.json')


def load_json(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


@click.group()
def cli():
    """Fitness Journal command line interface."""


@cli.command()
@click.option('--age', prompt=True, type=int)
@click.option('--gender', prompt=True)
@click.option('--goal', prompt=True)
@click.option('--weight', prompt='Current weight (kg)', type=float)
@click.option('--target', prompt='Target weight (kg)', type=float)
@click.option('--height', prompt='Height (cm)', type=float)
def setup(age, gender, goal, weight, target, height):
    """Set up or update user profile."""
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    profile = {
        'age': age,
        'gender': gender,
        'goal': goal,
        'current_weight': weight,
        'target_weight': target,
        'height_cm': height,
        'bmi': round(bmi, 1)
    }
    save_json(PROFILE_PATH, profile)
    click.echo(f"Profile saved. Your BMI is {profile['bmi']}")


@cli.command()
@click.option('--duration', prompt='Workout duration (minutes)', type=int)
def plan(duration):
    """Generate a workout plan for today."""
    profile = load_json(PROFILE_PATH, None)
    if not profile:
        click.echo('No profile found. Run "setup" first.')
        return
    workouts = load_json(WORKOUT_PATH, [])
    last_type = workouts[-1]['type'] if workouts else None
    next_type = 'strength' if last_type != 'strength' else 'cardio'
    workout = {
        'date': date.today().isoformat(),
        'type': next_type,
        'duration_minutes': duration
    }
    workouts.append(workout)
    save_json(WORKOUT_PATH, workouts)
    click.echo(f"Planned {next_type} workout for {duration} minutes")


if __name__ == '__main__':
    cli()
