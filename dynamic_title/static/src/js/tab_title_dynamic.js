/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { WebClient } from "@web/webclient/webclient";
import { useService, onWillUnmount } from "@odoo/owl";

patch(WebClient.prototype, {
  setup() {
    this._super = super.setup?.bind(this) || (() => {});
    this._super();
    // // console.log(" WebClient Patch Initialized!");

    // Ensure env and services exist
    if (!this.env || !this.env.services) {
      // // console.error(" this.env or this.env.services is undefined!");
      return;
    }

    this.bus = this.env.services.bus_service;
    if (!this.bus) {
      // // console.error(" bus_service is undefined!");
      return;
    }

    this._handleCurrentActionUpdated = this._updateTabTitle.bind(this);
    this._handleRecordUpdated = this._updateTabTitle.bind(this);

    // Subscribe to events
    this.bus.addEventListener(
      "CURRENT_ACTION_UPDATED",
      this._handleCurrentActionUpdated
    );
    this.bus.addEventListener("RECORD_UPDATED", this._handleRecordUpdated);

    // Unsubscribe when the component is destroyed
    onWillUnmount(() => {
      // // console.log(" Removing event listeners...");
      this.bus.removeEventListener(
        "CURRENT_ACTION_UPDATED",
        this._handleCurrentActionUpdated
      );
      this.bus.removeEventListener("RECORD_UPDATED", this._handleRecordUpdated);
    });

    //Add a delay before updating the tab title
    // setTimeout(function, delay)
    //     function: The function you want to execute after the delay.
    //     delay: The time in milliseconds to wait before executing the function.
    setTimeout(() => {
      // console.log(" Component Mounted! Updating tab title...");
      this._updateTabTitle();
    }, 1000); // Wait 1 second to ensure data is available
  },

  _updateTabTitle() {
    // console.log(" Updating Tab Title function called!");

    // Ensure env and services exist before proceeding
    if (!this.env || !this.env.services) {
      // console.error(" this.env or this.env.services is undefined!");
      return;
    }

    const actionService = this.env.services.action;
    const menuService = this.env.services.menu;

    if (!actionService) {
      // console.error(" actionService is undefined!");
      return;
    }

    const currentController = actionService.currentController;
    const currentAction = currentController?.action || "Unknown Action";

    // console.log(" Current Action:", currentAction);
    // console.log(" Current Controller:", currentController);

    let titleParts = [];

    // 1. Get Menu Name
    const activeMenu = menuService.getMenu(actionService.currentController?.action?.id);
    // const activeMenu = menuService.getMenu(
    //   menuService.currentController?.action?.id || menuService.activeMenuId
    // ); 
    // console.log(" Active Menu:", activeMenu);
    // if (activeMenu?.name) {
    //   titleParts.push(activeMenu.name);
    // }

    // 2. Get Action Name
    if (currentAction !== "Unknown Action") {
      titleParts.push(currentAction.name);
    }

    // **3. Get Record Name from Form View**
    if (currentController?.props?.record?.display_name) {
      titleParts.push(currentController.props.record.display_name);
    }
    const recordDisplayName = currentController?.displayName || "Unnamed Record";  // Fallback if displayName is missing
    console.log(" Record Display Name:", recordDisplayName);
    titleParts.push(recordDisplayName);

    // 4. Update Document Title
     const newTitle = `Cielo - ${titleParts.join("/")}`;

    console.log("📝 New Title:", newTitle);
    document.title = newTitle;

  },
  // Optional function to trigger action reload (instead of a full page reload)
  _reloadCurrentAction() {
    // console.log("🔄 Reloading current action...");

    // Get the current controller's action to determine the model dynamically
    const actionService = this.env.services.action;
    const currentController = actionService.currentController;
    const currentAction = currentController?.action;

    // Ensure currentAction and model are available
    if (!currentAction || !currentController?.props?.record?.id) {
      // // console.error(" currentAction or record id is missing!");
      return;
    }
    // Dynamically get the model name from the current action
    const resModel = currentAction.res_model; 
    // // console.log(" Reloading for model:", resModel);
    this.env.services.action.doAction({
      type: 'ir.actions.act_window',
      res_model: resModel,  // Use dynamic res_model here
      views: [[false, 'form']], // Adjust based on the view you want to reload (e.g., form, list)
      target: 'current',
      res_id: currentController?.props?.record?.id,  // Pass the record ID here
    });}
  
});


