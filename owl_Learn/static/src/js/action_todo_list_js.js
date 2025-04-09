/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onWillStart, useRef } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class webTodolist extends Component {
  setup() {
    // Initialize state
    this.state = useState({
      task: { name: "", color: "#FF0000", completed: false },
      taskList: [
        //   {id:1,name:"Task1",color:"#FF0000",completed:true},
        //   {id:2,name:"Task2",color:"#000000",completed:true},
        //   {id:3,name:"Task3",color:"#FFFFFF",completed:true},
        //   {id:4,name:"Task4",color:"#26B572",completed:true},
      ],
      isEdit: false,
      activeId: false,
    });
    // this.orm=useService("orm")
    // onWillStart(async()=>{
    //     this.state.taskList=await this.orm.searchRead("owl.todolist",[],['name','color','completed'])
    // })
    this.orm = useService("orm");
    this.model = "owl.todolist"; // Used for referenceing the model
    this.searchInput = useRef("searchInput");
    onWillStart(async () => {
      await this.getAllTasks();
    });
  }

  //   async getAllTasks()	Declares an async function
  // this.orm.searchRead(...)	Queries Odoo's ORM for data
  // this.model	Specifies the Odoo model (e.g., "owl.todolist")
  // await	Waits for the data before proceeding
  // this.state.taskList = ...	Stores data in the reactive state, triggering a UI update
  async getAllTasks() {
    this.state.taskList = await this.orm.searchRead(
      this.model,
      [],
      ["name", "color", "completed"]
    );
  }
  addTask() {
    this.resetForm();
    this.state.activeId = false;
    this.state.isEdit = false;
  }
  editTask(task) {
    this.state.activeId = task.id;
    this.state.isEdit = true;
    this.state.task = { ...task };
  }
  async saveTask() {
    if (!this.state.isEdit) {
      await this.orm.create(this.model, [this.state.task]);
    } else {
      await this.orm.write(this.model, [this.state.activeId], this.state.task);
    }
    // await this.orm.create(this.model, [
    //     this.state.task
    // //   {
    // //     name: this.state.task.name,
    // //     color: this.state.task.color,
    // //     completed: this.state.task.completed,
    // //   },
    // ]);

    await this.getAllTasks();
    console.log(this.state.name);
  }
  resetForm() {
    this.state.task = { name: "", color: "#FF0000", completed: false };
  }
  // async deleteTask() {
  //   await this.orm.unlink(this.model, [task.id]);
  //   await this.getAllTasks();
  // }
  
  async deleteTask(task) {
    if (!task || !task.id) {
        console.error("Error: Task is undefined or missing an ID", task);
        return;
    }

    try {
        await this.orm.unlink(this.model, [task.id]);
        await this.getAllTasks();  // Refresh the task list
        console.log(`Task ${task.id} deleted successfully.`);
    } catch (error) {
        console.error("Error deleting task:", error);
    }
}


  async toggletask(task) {
    if (!task || !task.id) {
        console.error("Error: Task is undefined or missing an ID", task);
        return;
    }

    try {
        await this.orm.write(this.model, [task.id], { completed: !task.completed });
        await this.getAllTasks();
        console.log(`Task ${task.id} toggled successfully.`);
    } catch (error) {
        console.error("Error updating task:", error);
    }
}


  // async searchTask() {
  //   const text = this.searchInput.el.value.trim();
  //   console.log(text);
  //   this.state.taskList = await this.orm.searchRead(
  //     // [["field_name", "operator", "value"]]
  //   // Fix: [[name, "ilike", Text]] → [['name', 'ilike', text]]
  //     this.model,[['name', "ilike", Text]], ["name", "color", "completed"]);
  // }

  async searchTask() {
    if (!this.searchInput || !this.searchInput.el) {
      console.error("Search input field is not available!");
      return;
    }

    const text = this.searchInput.el.value.trim(); // ✅ Fix variable case
    console.log("Searching for:", text);

    if (text) {
      try {
        this.state.taskList = await this.orm.searchRead(
          this.model,
          //   this.state.taskList = await this.orm.searchRead(
          // [["field_name", "operator", "value"]]
          [["name", "ilike", text]], // ✅ Corrected domain syntax
          ["name", "color", "completed"]
        );
        console.log("Search results:", this.state.taskList);
      } catch (error) {
        console.error("Search error:", error);
      }
    } else {
      console.warn("Empty search input, fetching all tasks...");
      await this.getAllTasks(); // ✅ Show all tasks if input is empty
    }
  }
}

// ✅ Ensure this matches the `t-name` in the XML template1
webTodolist.template = "owl_Learn.webTodolist";

// ✅ Ensure the registry key matches what you call in Odoo actions
registry.category("actions").add("owl_Learn.action_todo_list_js", webTodolist);

// ✅ Debugging log to confirm component registration
// console.log("OwlTodolist registered as 'owl_Learn.action_todo_list_js'");
