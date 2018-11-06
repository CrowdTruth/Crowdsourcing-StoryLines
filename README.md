# CrowdTruth ground truth for identifying Causal Relations between Events

Crowdsourced ground truth dataset for 1,204 sentences and 7,778 event pairs covering 22 news topics. The corpus was created by using the CrowdTruth methodology, as described in the following paper:

* Tommaso Caselli and Oana Inel: [Crowdsourcing StoryLines: Harnessing the Crowd for Causal Relation Annotation](http://eventstory.news.s3-website-us-west-2.amazonaws.com/2018workshop_menu/W18-4306.pdf). [Events and Stories in the News Workshops, COLING 2018](http://www.eventstory.news)

If you find this data useful in your research, please consider citing:

```
@inproceedings{caselli2018crowdsourcing,
  title={Crowdsourcing StoryLines: Harnessing the Crowd for Causal Relation Annotation},
  author={Caselli, Tommaso and Inel, Oana},
  booktitle={Proceedings of the Workshop Events and Stories in the News 2018},
  pages={44--54},
  year={2018}
}
```

Crowdsourcing results and evaluation against expert data are available in folder:
``` |--data/results/ ```

Expert ground truth data is available in folder:
``` |--data/ground_truth/ ```

Aggregated raw crowdsourcig data is available in folder:
``` |--data/aggregated_input/ ```

Raw crowdsourcig data is available in folder:
``` |--data/input/ ```


## Running the notebooks

To run and regenerate the results, you need to install the stable version of the **crowdtruth==2.0** package from PyPI using:
```
pip install crowdtruth==2.0
```
