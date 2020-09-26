from feather.managers.output_manager import OutputManager


def test_that_output_manager_updates_history():
    output_manager = OutputManager()

    output_manager.print("intro")
    output_manager.save_input("input1")
    output_manager.print("output1")
    output_manager.print("output2")

    output_manager.save_input("input2")
    output_manager.print("output3")

    assert output_manager.history == [
        {
            "output": "intro"
        },
        {
            "input": "input1",
            "outputs": ["output1", "output2"]
        },
        {
            "input": "input2",
            "outputs": ["output3"]
        },
    ]
