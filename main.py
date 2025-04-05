from final_evaluation import (finalEvaluation)
from export_table import export_table_png
from tabulate import tabulate


def exp_print(iou, precision, recall, info):
    print("-"*20)
    print("Experiment number", exp_num)
    print(f"t_e ∩ t_r: {info[0]}, t_e: {info[1]}, t_r: {info[2]}")
    print("IoU: ", iou)
    print("precision:", precision)
    print("recall", recall)


def run_experiment(chunk_size, chunk_overlap, top_k):
    global exp_num
    exp_num += 1
    iou, recall, precision, info = finalEvaluation(chunk_size, chunk_overlap, top_k)
    exp_print(iou, precision, recall, info)
    result = {
        "chunk_size": int(chunk_size),
        "chunk_overlap": int(chunk_overlap),
        "top_k": int(top_k),
        "recall": recall,
        "precision": precision,
        "IoU": iou
    }
    result_list.append(result)


exp_num = 0
result_list = []
run_experiment(800, 400, 10)
run_experiment(400, 200, 10)
run_experiment(400, 0, 10)
run_experiment(300, 0, 10)
run_experiment(200, 0, 10)
run_experiment(100, 0, 10)
run_experiment(800, 400, 5)
run_experiment(400, 200, 5)
run_experiment(400, 0, 5)
run_experiment(300, 0, 5)
run_experiment(200, 0, 5)
run_experiment(100, 0, 5)
run_experiment(800, 400, 2)
run_experiment(400, 200, 2)
run_experiment(400, 0, 2)
run_experiment(300, 0, 2)
run_experiment(200, 0, 2)
run_experiment(100, 0, 2)


print(tabulate(result_list, headers="keys", tablefmt="grid"))

pict_dir = "result_tables"
export_table_png(result_list, pict_dir+"/final_evaluation_results.png")
