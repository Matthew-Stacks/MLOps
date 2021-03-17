<div align="center">
<h1><img width="30" src="https://madewithml.com/static/images/rounded_logo.png">&nbsp;<a href="https://madewithml.com/">Made With ML</a></h1>
Applied ML · MLOps · Production
<br>
Join 20K+ developers in learning how to responsibly <a href="https://madewithml.com/about/">deliver value</a> with applied ML.
</div>

<br>

<div align="center">
    <a target="_blank" href="https://newsletter.madewithml.com"><img src="https://img.shields.io/badge/Subscribe-20K-brightgreen"></a>&nbsp;
    <a target="_blank" href="https://github.com/GokuMohandas/madewithml"><img src="https://img.shields.io/github/stars/GokuMohandas/madewithml.svg?style=social&label=Star"></a>&nbsp;
    <a target="_blank" href="https://www.linkedin.com/in/goku"><img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social"></a>&nbsp;
    <a target="_blank" href="https://twitter.com/GokuMohandas"><img src="https://img.shields.io/twitter/follow/GokuMohandas.svg?label=Follow&style=social"></a>
</div>

<br>

> If you need refresh yourself on ML algorithms, check out our [ML Foundations](https://github.com/GokuMohandas/madewithml) repository (🔥&nbsp; Among the <a href="https://github.com/topics/deep-learning" target="_blank">top ML</a> repositories on GitHub)

<br>

<table>
    <tr>
        <td align="center"><b>📦&nbsp; Product</b></td>
        <td align="center"><b>🔢&nbsp; Data</b></td>
        <td align="center"><b>📈&nbsp; Modeling</b></td>
    </tr>
    <tr>
        <td><a href="https://madewithml.com/courses/applied-ml/objective/">Objective</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/annotation/">Annotation</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/baselines/">Baselines</a></td>
    </tr>
    <tr>
        <td><a href="https://madewithml.com/courses/applied-ml/solution/">Solution</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/exploratory-data-analysis/">Exploratory data analysis</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/experiment-tracking/">Experiment tracking</a></td>
    </tr>
    <tr>
        <td><a href="https://madewithml.com/courses/applied-ml/evaluation/">Evaluation</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/splitting/">Splitting</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/optimization/">Optimization</a></td>
    </tr>
    <tr>
        <td><a href="https://madewithml.com/courses/applied-ml/iteration/">Iteration</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/preprocessing/">Preprocessing</a></td>
        <td></td>
    </tr>
</table>

<table>
    <tr>
        <td align="center"><b>📝&nbsp; Scripting</b></td>
        <td align="center"><b>(cont.)</b></td>
        <td align="center"><b>📦&nbsp; Application</b></td>
        <td align="center"><b>✅&nbsp; Testing</b></td>
    </tr>
    <tr>
        <td><a href="https://madewithml.com/courses/applied-ml/organization/">Organization</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/styling/">Styling</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/cli/">CLI</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/testing/">Code</a></td>
    </tr>
    <tr>
        <td><a href="https://madewithml.com/courses/applied-ml/packaging/">Packaging</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/makefile/">Makefile</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/api/">API</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/testing/#data">Data</a></td>
    </tr>
    <tr>
        <td><a href="https://madewithml.com/courses/applied-ml/documentation/">Documentation</a></td>
        <td><a href="https://madewithml.com/courses/applied-ml/logging/">Logging</a></td>
        <td></td>
        <td><a href="https://madewithml.com/courses/applied-ml/testing/#models">Models</a></td>
    </tr>
</table>

<table>
    <tr>
        <td align="center"><b>⏰&nbsp; Version control</b></td>
        <td align="center"><b>🚀&nbsp; Production</b></td>
        <td align="center"><b>(cont.)</b></td>
    </tr>
    <tr>
        <td>Git</td>
        <td>Dashboard</td>
        <td>Feature stores</td>
    </tr>
    <tr>
        <td>Precommit</td>
        <td>Docker</td>
        <td>Workflows</td>
    </tr>
    <tr>
        <td>Versioning</td>
        <td>CI/CD</td>
        <td>Active learning</td>
    </tr>
    <tr>
        <td></td>
        <td>Monitoring</td>
        <td></td>
    </tr>
</table>

📆&nbsp; new lesson every week!<br>
<a href="https://newsletter.madewithml.com" target="_blank">Subscribe</a> for our monthly updates on new content.

<br>

## Directory structure
```bash
app/
├── api.py        - FastAPI app
└── cli.py        - CLI app
├── schemas.py    - API model schemas
tagifai/
├── config.py     - configuration setup
├── data.py       - data processing components
├── eval.py       - evaluation components
├── main.py       - training/optimization pipelines
├── models.py     - model architectures
├── predict.py    - inference components
├── train.py      - training components
└── utils.py      - supplementary utilities
```
> Documentation for this application can be found [here](https://gokumohandas.github.io/applied-ml/).

## Workflows

### Use existing model

1. Set up environment.
```bash
export venv_name="venv"
make venv name=${venv_name} env="prod"
source ${venv_name}/bin/activate
```

2. Pull latest model.
```bash
dvc pull experiments
tagifai fix-artifact-metadata
```

3. Run Application
```bash
make app env="dev"
```
You can interact with the API directly or explore via the generated documentation at [http://0.0.0.0:5000/docs](http://0.0.0.0:5000/docs).

### Update model (CI/CD)
Coming soon after CI/CD lesson where the entire application will be retrained and deployed when we push new data (or trigger manual reoptimization/training). The deployed model, with performance comparisons to previously deployed versions, will be ready on a PR to push to the main branch.

### Update model (manual)

1. Set up the development environment.
```bash
export venv_name="venv"
make venv name=${venv_name} env="dev"
source ${venv_name}/bin/activate
```

2. Pull versioned data.
```bash
dvc pull data/tags.json
dvc pull data/projects.json
```

3. Optimize using distributions specified in `tagifai.main.objective`. This also writes the best model's args to [config/args.json](https://github.com/GokuMohandas/applied-ml/blob/main/config/args.json)
```bash
tagifai optimize \
    --args-fp config/args.json \
    --study-name optimization \
    --num-trials 100
```
> We'll cover how to train using compute instances on the cloud from Amazon Web Services (AWS) or Google Cloud Platforms (GCP) in later lessons. But in the meantime, if you don't have access to GPUs, check out the [optimize.ipynb](https://colab.research.google.com/github/GokuMohandas/applied-ml/blob/main/notebooks/optimize.ipynb) notebook for how to train on Colab and transfer to local. We essentially run optimization, then train the best model to download and transfer it's arguments and artifacts. Once we have them in our local machine, we can run `tagifai fix-artifact-metadata` to match all metadata as if it were run from your machine.

4. Train a model (and save all it's artifacts) using args from [config/args.json](https://github.com/GokuMohandas/applied-ml/blob/main/config/args.json) and publish metrics to [metrics/performance.json](https://github.com/GokuMohandas/applied-ml/blob/main/metrics/performance.json). You can view the entire run's details inside `experiments/{experiment_id}/{run_id}` or via the API (`GET` /runs/{run_id}).
```bash
tagifai train-model \
    --args-fp config/args.json \
    --experiment-name best \
    --run-name model \
    --publish-metrics  # save to metrics/performance.json
```

5. Predict tags for an input sentence. It'll use the best model saved from `train-model` but you can also specify a `run-id` to choose a specific model.
```bash
tagifai predict-tags --text "Transfer learning with BERT"  # test with CLI app
make app env="dev"  # run API and test if you want
```

6. View improvements
Once you're done training the best model using the current data version, best hyperparameters, etc., we can view performance difference.
```bash
tagifai diff --commit-a workspace --commit-b HEAD
```

7. Commit to git
This will clean and update versioned assets (data, experiments), run tests, styling, etc.
```bash
git add .
git commit -m ""
<precommit (dvc, tests, style, clean, etc.) will execute>
git push origin main
```

## Commands

### Application
```bash
make app  # uvicorn app.api:app --host 0.0.0.0 --port 5000 --reload --reload-dir tagifai --reload-dir app
make app-prod  # gunicorn -c config/gunicorn.py -k uvicorn.workers.UvicornWorker app.api:app
```

### Streamlit dashboard
```bash
make streamlit  # streamlit run streamlit/app.py
```

### MLFlow
```bash
make mlflow  # mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri experiments/
```

### Mkdocs
```bash
make docs  # python -m mkdocs serve
```

### Testing
```bash
make great-expectations  # great_expectations checkpoint run [projects, tags]
make test  # pytest --cov tagifai --cov app --cov-report html
make test-non-training  # pytest -m "not training"
```

### Start Jupyterlab
```bash
python -m ipykernel install --user --name=tagifai
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install @jupyterlab/toc
jupyter lab
```
> You can also run all notebooks on [Google Colab](https://colab.research.google.com/github/GokuMohandas/applied-ml/blob/main/notebooks/tagifai.ipynb).


## FAQ

### Why is this free?
While this content is for everyone, it's especially targeted towards people who don't have as much opportunity to learn. I firmly believe that creativity and intelligence are randomly distributed but opportunity is siloed. I want to enable more people to create and contribute to innovation.

### Who is the author?
- I've deployed large scale ML systems at Apple as well as smaller systems with constraints at startups and want to share the common principles I've learned along the way.
- I created [Made With ML](https://madewithml.com/) so that the community can explore, learn and build ML and I learned how to build it into an end-to-end product that's currently used by over 20K monthly active users.
- Connect with me on <a href="https://twitter.com/GokuMohandas" target="_blank"><i class="fab fa-twitter ai-color-info mr-1"></i>Twitter</a> and <a href="https://www.linkedin.com/in/goku" target="_blank"><i class="fab fa-linkedin ai-color-primary mr-1"></i>LinkedIn</a>

<!-- Citation -->
<hr>
To cite this course, please use:

```bash
@article{madewithml,
    title  = "Applied ML - Made With ML",
    author = "Goku Mohandas",
    url    = "https://madewithml.com/courses/applied-ml/"
    year   = "2021",
}
```