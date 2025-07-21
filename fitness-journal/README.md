# Fitness Journal

A small command line application to record your fitness profile and generate daily workout plans.

## Usage

1. Install dependencies (they are already included in this repository but can also be installed from `requirements.txt`):

```bash
pip install -r requirements.txt
```

2. Initialize your profile:

```bash
python fitness_journal.py setup
```

You will be prompted for your age, gender, goal, weight, target weight and height. The application will calculate your BMI and store your profile.

3. Create a new workout plan for the day:

```bash
python fitness_journal.py plan --duration 30
```

A workout will be planned based on your last recorded workout so that you alternate between cardio and strength days. Plans are stored in `fitness_data/workouts.json`.

## Files

- `fitness_journal.py` – the command line entry point.
- `requirements.txt` – Python dependencies.
- Data is stored under `fitness_data/`.
