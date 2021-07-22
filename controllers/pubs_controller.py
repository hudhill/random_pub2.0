from flask import Flask, render_template, redirect, request
from flask import Blueprint
from console import populate_db

from models.pub import Pub
import repositories.pub_repository as pub_repository

pubs_blueprint = Blueprint("pubs", __name__)

@pubs_blueprint.route("/pub")
def get_random_pub():
  pubs = pub_repository.select_all()
  pub = pub_repository.get_pub(pubs)

  return render_template("show.html", pub=pub)

# creating a populate route that when run takes a function from console.py that populates the db
@pubs_blueprint.route("/populate")
def populate():
  populate_db()
  return "done"