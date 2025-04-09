/** @odoo-module */

import { registry } from "@web/core/registry";
const { Component, onWillStart, onMounted, useState } = owl;
import { jsonrpc } from "@web/core/network/rpc_service";
import { useService } from "@web/core/utils/hooks";

export class ProjectDashboard extends Component {
  setup() {
    this.action = useService("action");
    this.project_state = useState({
      projects_count: 0,
      project_ids: [],
    });

    onWillStart(this.onWillStart);
    onMounted(this.onMounted);
    this.chart_state = useState({
      chartTypes: ['bar', 'line', 'pie', 'doughnut', 'radar', 'polarArea', 'bubble', 'scatter'], // Array of all chart types
      currentChartIndex: 0, // Track the current chart index
    });
    this.chart = null; // To hold the chart instance
  }

  async onWillStart() {
    await this.fetchDataProject();
  }

  async onMounted() {
    this.render_projects_hours();
  }

  fetchDataProject() {
    var self = this;
    jsonrpc("/get/project/data", {}).then(function (data_result) {
      console.log("Projects Count:", data_result.projects_count);
      console.log("Project IDs:", data_result.project_ids);
      self.project_state.projects_count = data_result.projects_count;
      self.project_state.project_ids = data_result.project_ids;
    });
  }

  toggleChart() {
    // Cycle through all chart types
    this.chart_state.currentChartIndex = (this.chart_state.currentChartIndex + 1) % this.chart_state.chartTypes.length;
    this.render_projects_hours();  // Re-render the chart with the new type
  }

  render_projects_hours() {
    const ctx = document.querySelector('.project_hours');  // Use native DOM method
    if (this.chart) {
      this.chart.destroy();  // Destroy the previous chart
    }

    const data = {
      labels: ["ProjectA", "ProjectB", "ProjectC"],
      datasets: [
        {
          label: "Dataset",
          data: [100, 200, 300],
          backgroundColor: [
            "rgb(255, 99, 132)",
            "rgb(54, 162, 235)",
            "rgb(255, 205, 86)",
          ],
          hoverOffset: 4,
        },
      ],
    };

    // Initialize a new chart using the current chart type
    this.chart = new Chart(ctx, {
      type: this.chart_state.chartTypes[this.chart_state.currentChartIndex],  // Use the current chart type
      data: data,
    });
  }

  _onClickProjects() {
    var project_ids = this.project_state.project_ids;
    var options = {
      additional_context: {},
      clearBreadcrumbs: false,
    };
    this.action.doAction(
      {
        name: "projects",
        type: "ir.actions.act_window",
        res_model: "project.project",
        view_model: "form",
        views: [
          [false, "list"],
          [false, "form"],
        ],
        domain: [["id", "in", project_ids]],
        context: {
          create: false,
        },
        target: "current",
      },
      options
    );
    console.log(project_ids);
  }
}

ProjectDashboard.template = "ProjectDashBoardMain";
registry.category("actions").add("project_dashboard_main", ProjectDashboard);


// /** @odoo-module */

// import { registry } from "@web/core/registry";
// const { Component, onWillStart, onMounted, useState } = owl;
// import { jsonrpc } from "@web/core/network/rpc_service";
// import { useService } from "@web/core/utils/hooks";

// export class ProjectDashboard extends Component {
//   setup() {
//     this.action = useService("action");
//     this.project_state = useState({
//       projects_count: 0,
//       project_ids: [],
//     });

//     onWillStart(this.onWillStart);
//     onMounted(this.onMounted);
//     this.chart_state = useState({
//       chartTypes: ['line', 'bar', 'pie', 'doughnut', 'radar', 'polarArea', 'bubble', 'scatter'], // Array of all chart types
//       currentChartIndex: 0, // Track the current chart index
//     });
//     this.chart = null; // To hold the chart instance
//   }

//   async onWillStart() {
//     await this.fetchDataProject();
//   }

//   async onMounted() {
//     this.render_projects_hours();
//   }

//   fetchDataProject() {
//     var self = this;
//     jsonrpc("/get/project/data", {}).then(function (data_result) {
//       console.log("Projects Count:", data_result.projects_count);
//       console.log("Project IDs:", data_result.project_ids);
//       self.project_state.projects_count = data_result.projects_count;
//       self.project_state.project_ids = data_result.project_ids;
//     });
//   }

//   toggleChart() {
//     // Cycle through all chart types
//     this.chart_state.currentChartIndex = (this.chart_state.currentChartIndex + 1) % this.chart_state.chartTypes.length;
//     this.render_projects_hours();  // Re-render the chart with the new type
//   }

//   render_projects_hours() {
//     const ctx = document.querySelector('.project_hours');  // Use native DOM method
//     if (this.chart) {
//       this.chart.destroy();  // Destroy the previous chart
//     }

//     const data = {
//       labels: ["ProjectA", "ProjectB", "ProjectC","ProjectD"],
//       datasets: [
//         {
//           label: "Dataset",
//           data: [240, 120, 380,80],
//           backgroundColor: [
//             "rgb(255, 99, 132)",
//             "rgb(54, 162, 235)",
//             "rgb(255, 205, 86)",
//             "   rgba(86,255,89)",
//           ],
//           hoverOffset: 4,
//         },
//       ],
//     };

//     // Initialize a new chart using the current chart type
//     this.chart = new Chart(ctx, {
//       type: this.chart_state.chartTypes[this.chart_state.currentChartIndex],  // Use the current chart type
//       data: data,
//     });
//   }

//   _onClickProjects() {
//     var project_ids = this.project_state.project_ids;
//     var options = {
//       additional_context: {},
//       clearBreadcrumbs: false,
//     };
//     this.action.doAction(
//       {
//         name: "projects",
//         type: "ir.actions.act_window",
//         res_model: "project.project",
//         view_model: "form",
//         views: [
//           [false, "list"],
//           [false, "form"],
//         ],
//         domain: [["id", "in", project_ids]],
//         context: {
//           create: false,
//         },
//         target: "current",
//       },
//       options
//     );
//     console.log(project_ids);
//   }
// }

// ProjectDashboard.template = "ProjectDashBoardMain";
// registry.category("actions").add("project_dashboard_main", ProjectDashboard);

// // /** @odoo-module */

// // import { registry } from "@web/core/registry";
// // const { Component, onWillStart, onMounted, useState } = owl;
// // import { jsonrpc } from "@web/core/network/rpc_service";
// // import { useService } from "@web/core/utils/hooks";

// // export class ProjectDashboard extends Component {
// //   setup() {
// //     this.action = useService("action");
// //     this.project_state = useState({
// //       projects_count: 0,
// //       project_ids: [],
// //     });

// //     onWillStart(this.onWillStart);
// //     onMounted(this.onMounted);
// //     this.chart_state = useState({
// //       chartType: 'bar', // default chart type
// //     });
// //     this.chart = null; // To hold the chart instance
// //   }

// //   async onWillStart() {
// //     await this.fetchDataProject();
// //   }

// //   async onMounted() {
// //     this.render_projects_hours();
// //   }

// //   fetchDataProject() {
// //     var self = this;
// //     jsonrpc("/get/project/data", {}).then(function (data_result) {
// //       console.log("Projects Count:", data_result.projects_count);
// //       console.log("Project IDs:", data_result.project_ids);
// //       self.project_state.projects_count = data_result.projects_count;
// //       self.project_state.project_ids = data_result.project_ids;
// //     });
// //   }

// //   toggleChart() {
// //     this.chart_state.chartType = this.chart_state.chartType === 'bar' ? 'doughnut' : 'bar';
// //     this.render_projects_hours();  // Re-render the chart with the new type
// //   }

// //   render_projects_hours() {
// //     const ctx = document.querySelector('.project_hours');  // Use native DOM method
// //     if (this.chart) {
// //       this.chart.destroy();  // Destroy the previous chart
// //     }

// //     const data = {
// //       labels: ["ProjectA", "ProjectB", "ProjectC"],
// //       datasets: [
// //         {
// //           label: "Dataset",
// //           data: [100, 200, 300],
// //           backgroundColor: [
// //             "rgb(255, 99, 132)",
// //             "rgb(54, 162, 235)",
// //             "rgb(255, 205, 86)",
// //           ],
// //           hoverOffset: 4,
// //         },
// //       ],
// //     };

// //     // Initialize a new chart
// //     this.chart = new Chart(ctx, {
// //       type: this.chart_state.chartType,  // Use the current chart type
// //       data: data,
// //     });
// //   }

// //   _onClickProjects() {
// //     var project_ids = this.project_state.project_ids;
// //     var options = {
// //       additional_context: {},
// //       clearBreadcrumbs: false,
// //     };
// //     this.action.doAction(
// //       {
// //         name: "projects",
// //         type: "ir.actions.act_window",
// //         res_model: "project.project",
// //         view_model: "form",
// //         views: [
// //           [false, "list"],
// //           [false, "form"],
// //         ],
// //         domain: [["id", "in", project_ids]],
// //         context: {
// //           create: false,
// //         },
// //         target: "current",
// //       },
// //       options
// //     );
// //     console.log(project_ids);
// //   }
// // }

// // ProjectDashboard.template = "ProjectDashBoardMain";
// // registry.category("actions").add("project_dashboard_main", ProjectDashboard);













// // // /** @odoo-module */

// // // import { registry } from "@web/core/registry";
// // // const { Component, onWillStart, onMounted, useState } = owl;
// // // import { jsonrpc } from "@web/core/network/rpc_service";
// // // import { useService } from "@web/core/utils/hooks";

// // // export class ProjectDashboard extends Component {
// // //   setup() {
// // //     this.action = useService("action");
// // //     this.project_state = useState({
// // //       projects_count: 0,
// // //       project_ids: [],
// // //     });

// // //     onWillStart(this.onWillStart);
// // //     onMounted(this.onMounted);
// // //     this.chart_state = useState({
// // //         chartType: 'bar', // default chart type
// // //       });
// // //   }
// // //   async onWillStart() {
// // //     await this.fetchDataProject();
// // //   }
// // //   async onMounted() {
// // //     this.render_projects_hours();
// // //   }

// // //   fetchDataProject() {
// // //     var self = this;
// // //     jsonrpc("/get/project/data", {}).then(function (data_result) {
// // //       // Log the result to the console
// // //       console.log("Projects Count:", data_result.projects_count);
// // //       console.log("Project IDs:", data_result.project_ids);
// // //       self.project_state.projects_count = data_result.projects_count;
// // //       self.project_state.project_ids = data_result.project_ids;
// // //     });
// // //   }

// // //   //   render_projects_hours() {
// // //   //     var self = this;
// // //   //     var ctx = $('.project_hours')
// // //   //     var data = {
// // //   //         labels: [
// // //   //             'ProA',
// // //   //             'ProjB',
// // //   //             'ProjC'
// // //   //         ],
// // //   //         datasets: [
// // //   //             {
// // //   //                 label: "Dataset",
// // //   //                 data: [100, 200, 300],
// // //   //                 backgroundColor: [
// // //   //                     'rgb(255, 99, 132)',
// // //   //                     'rgb(54, 162, 235)',
// // //   //                     'rgb(255, 205, 86)'
// // //   //                 ],
// // //   //                 hoverOffset: 4
// // //   //             }
// // //   //         ]
// // //   //     }

// // //   //     var chart = new Chart(ctx, {
// // //   //         type: 'doughnut',
// // //   //         data: data,
// // //   //     });
// // //   // }
 
// // //   toggleChart() {
// // //     this.chart_state.chartType = this.chart_state.chartType === 'bar' ? 'doughnut' : 'bar';
// // //     this.render_projects_hours();  // Re-render the chart with the new type
// // //   }
// // //   render_projects_hours() {
// // //     var self = this;
// // //     var ctx = $(`.project_hours`);

// // //     var data = {
// // //       labels: ["ProjectA", "ProjectB", "ProjectC"],
// // //       datasets: [
// // //         {
// // //           label: "Dataset",
// // //           data: [100, 200, 300],
// // //           backgroundColor: [
// // //             "rgb(255, 99, 132)",
// // //             "rgb(54, 162, 235)",
// // //             "rgb(255, 205, 86)",
// // //           ],
// // //           hoverOffset: 4,
// // //         },
// // //       ],
// // //     };
// // //     var chart = new Chart(ctx, {
// // //         type: this.chart_state.chartType,  // Use the current chart type ('bar' or 'doughnut')
// // //         data: data,
// // //       });
// // //     // var chart = new Chart(ctx, {
// // //     //   type: "bar",
// // //     //   data: data,
// // //     // });
// // //   }
// // //   _onClickProjects() {
// // //     var project_ids = this.project_state.project_ids;
// // //     // if (project_ids)
// // //     var options = {
// // //       additional_context: {},
// // //       clearBreadcrumbs: false,
// // //     };
// // //     this.action.doAction(
// // //       {
// // //         name: "projects",
// // //         type: "ir.actions.act_window",
// // //         res_model: "project.project",
// // //         view_model: "form",
// // //         views: [
// // //           [false, "list"],
// // //           [false, "form"],
// // //         ],
// // //         doamin: [["id", "in", "project_ids"]],
// // //         context: {
// // //           create: false,
// // //         },
// // //         target: "current",
// // //       },
// // //       options
// // //     );
// // //     s;
// // //     console.log(project_ids);
// // //     //   Action = way 2
// // //     // let xml_id = "project.open_view_project_all_config";
// // //     // this.action.doAction(xml_id, {
// // //     //   options,
// // //     // });
// // //   }
// // // }

// // // ProjectDashboard.template = "ProjectDashBoardMain";
// // // registry.category("actions").add("project_dashboard_main", ProjectDashboard);
