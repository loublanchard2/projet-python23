from gflow.utils.plot_utils import PlotTrajectories
from gflow.cases import Cases
from gflow.utils.simulation_utils import run_simulation

if __name__ == "__main__":
    file_name = "cases.json"
    case_name = "random5"

    case = Cases.get_case(filename=file_name, case_name=case_name)

    run_simulation(
        case,
        t=20000,  # maximum number of timesteps
        update_every=1,  # leave as 1
        stop_at_collision=False,  # leave as False
        max_avoidance_distance=999999,  # larger than simulation domain
    )

    trajectory_plot = PlotTrajectories(case, update_every=1)
    trajectory_plot.show()
