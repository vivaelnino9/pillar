import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { OrganizationListComponent } from './organization-list/organization-list.component';
import { OrganizationCreateComponent } from './organization-create/organization-create.component';

const routes: Routes = [
  { path: '', redirectTo: 'organizations', pathMatch: 'full' },
  {
    path: 'organizations',
    component: OrganizationListComponent
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
