GooglePlayStore::Application.routes.draw do
  # get '/', to: 'apps#list', as: 'show_all'
  get 'apps/details' => 'apps#show', :constraints => { :id => /[\w+\.]+/ }, as: 'get_app'

  # apps/developer/Facebook
  get 'apps/developer/:dev' => 'apps#list_by_dev', as: 'get_dev'

  # apps/developer?dev=
  get 'apps/developer' => 'apps#list_by_dev'

  # apps/search?q=
  get 'apps/search' => 'apps#list_by_search'

  root :to => 'apps#list', as: 'show_all'
end
