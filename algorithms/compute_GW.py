from .GromovWassersteinLearning import GromovWassersteinLearning
import torch.optim as optim
import torch



def GW_correspondence(database,lambda_T):
    opt_dict = {'epochs': 4,
                'batch_size': 20000,
                'use_cuda': True,
                'strategy': 'soft',
                'beta': 1e-2,
                'outer_iteration': 200,
                'inner_iteration': 1,
                'sgd_iteration': 150,
                'prior': False,
                'display': False}
    hyperpara_dict = {'src_number': len(database['src_index']),
                      'tar_number': len(database['tar_index']),
                      'dimension': 128,
                      'loss_type': 'L2',
                      'cost_type': 'cosine',
                      'ot_method': 'proximal'}

    gwd_model = GromovWassersteinLearning(hyperpara_dict)

    # initialize optimizer
    optimizer = optim.Adam(gwd_model.gwl_model.parameters(), lr=1e-3)

    # Gromov-Wasserstein learning
    trans = gwd_model.train_with_prior(database, optimizer, opt_dict, scheduler=None)
    trans = torch.tensor(trans)
    ind = torch.nonzero((trans > lambda_T) & (trans <= 1), as_tuple=False)

    correspondence = [[],[],[]]
    for i in range(ind.size(0)):
        temp = [[ind[i, 0]],[ind[i, 1]]]
        if temp in database['mutual_interactions2']:
            index = database['mutual_interactions2'].index(temp)
            correspondence[0].append(database['correspondence'][0][index])
            correspondence[1].append(database['correspondence'][1][index])
            correspondence[2].append(database['correspondence'][2][index])

    return correspondence, trans


