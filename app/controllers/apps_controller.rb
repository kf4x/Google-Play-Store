class AppsController < ApplicationController


  def show
    @app = App.find_by_package(params[:id])
    # puts(@app.description)

  end

  def list
    @apps = App.all
  end

end
