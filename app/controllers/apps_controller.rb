class AppsController < ApplicationController


  def show
    @app = App.find_by_package(params[:id])
    # puts(@app.description)

  end

  def list
    @apps = App.all
  end

  def list_by_search
    @apps = App.all
    render :layout => 'list'
  end

  def list_by_dev
    @apps = App.find_all_by_developer(params[:dev])

    render :template => 'apps/list'
  end

end
