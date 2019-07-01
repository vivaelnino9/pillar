import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { OrganizationListComponent } from './organization-list/organization-list.component';
import { OrganizationCreateComponent } from './organization-create/organization-create.component';
import { RepoListComponent } from './repo-list/repo-list.component';

const routes: Routes = [
  { path: '', redirectTo: 'organizations', pathMatch: 'full' },
  {
    path: 'organizations',
    component: OrganizationListComponent
  },
  {
    path: 'organizations/:id',
    component: RepoListComponent
  },
  {
    path: 'create-organization',
    component: OrganizationCreateComponent
  },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
